from enum import IntEnum
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db import connection, models
from django.urls import reverse
from django.utils.functional import cached_property
from django_intenum import IntEnumField
from hearthstone.enums import BnetRegion


HEARTHSTONE_LOCALES = (
	("enUS", "English"),
	# ("enGB", "English (GB)"),
	("zhTW", "Chinese (TW)"),
	("zhCN", "Chinese (CN)"),
	("frFR", "French"),
	("deDE", "German"),
	("itIT", "Italian"),
	("jaJP", "Japanese"),
	("koKR", "Korean"),
	("plPL", "Polish"),
	("ptBR", "Portuguese (BR)"),
	# ("ptPT", "Portuguese (PT)"),
	("ruRU", "Russian"),
	("esES", "Spanish (ES)"),
	("esMX", "Spanish (MX)"),
	("thTH", "Thai"),
)


class Visibility(IntEnum):
	Public = 1
	Unlisted = 2


class AccountClaim(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
	token = models.OneToOneField("accounts.AuthToken", on_delete=models.CASCADE)
	api_key = models.ForeignKey("api.APIKey", on_delete=models.CASCADE, null=True)
	created = models.DateTimeField("Created", auto_now_add=True)

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse("account_claim", kwargs={"id": self.id})

	def get_full_url(self):
		return "https://hsreplay.net" + self.get_absolute_url()


class User(AbstractUser):
	id = models.BigAutoField(primary_key=True)
	username = models.CharField(max_length=150, unique=True)
	battletag = models.CharField(
		max_length=24, blank=True,
		help_text="The user's primary Battle.net username."
	)
	is_fake = models.BooleanField(default=False)

	# Profile fields
	locale = models.CharField(
		max_length=8, default="enUS",
		choices=HEARTHSTONE_LOCALES,
		help_text="The user's preferred Hearthstone locale for display"
	)
	default_replay_visibility = IntEnumField(
		"Default replay visibility",
		enum=Visibility, default=Visibility.Public
	)
	exclude_from_statistics = models.BooleanField(default=False)
	joust_autoplay = models.BooleanField(default=True)
	settings = JSONField(default={}, blank=True)

	@cached_property
	def stripe_customer(self):
		from djstripe.models import Customer
		customer, created = Customer.get_or_create(self)
		return customer

	@cached_property
	def is_stripe_premium(self):
		"""
		Returns True if a user is Premium on a Stripe plan.
		"""
		# The following uses raw sql to avoid a dependency on dj-stripe.
		with connection.cursor() as cursor:
			cursor.execute("""
				select count(*) from djstripe_subscription ds where (
					ds.customer_id in (
						select djstripe_id from djstripe_customer where subscriber_id = %s
					) AND (
						ds.status = 'active' or ds.status = 'trialing'
					) AND
						ds.current_period_end > now()
				)
			""", (self.id, ))
			sub_count, = cursor.fetchone()
			if sub_count:
				return True
		return False

	@cached_property
	def is_paypal_premium(self):
		"""
		Returns True if a user is Premium on a Paypal plan.
		"""
		with connection.cursor() as cursor:
			cursor.execute("""
				select count(*) from djpaypal_billingagreement db where (
					db.state = 'Active' and
					db.end_of_period > CURRENT_TIMESTAMP - INTERVAL '15 days' and
					db.user_id = %s
				)
			""", (self.id, ))
			sub_count, = cursor.fetchone()
			if sub_count:
				return True

		if self.paypal_end_of_cancellation_period:
			return True

		return False

	@cached_property
	def paypal_end_of_cancellation_period(self):
		"""
		Returns the end date of the cancellation period, or None if expired.
		"""
		with connection.cursor() as cursor:
			cursor.execute("""
				select max(db.end_of_period) from
					djpaypal_billingagreement db
				where
					(db.state = 'Cancelled' or db.state = 'Canceled') and
					db.user_id = %s and
					db.end_of_period > now()
			""", (self.id, ))
			end_date, = cursor.fetchone()
		return end_date

	@cached_property
	def is_premium(self):
		# The PREMIUM_OVERRIDE setting allows forcing a True or False for all users
		# This is especially useful if no Stripe API key is available
		premium_override = getattr(settings, "PREMIUM_OVERRIDE", None)
		if premium_override is not None:
			return premium_override

		return self.is_stripe_premium or self.is_paypal_premium

	def delete_replays(self):
		self.replays.update(is_deleted=True)

	def guess_player_name(self):
		names = []
		for replay in self.replays.filter(spectator_mode=False):
			name = replay.friendly_player.name
			if name:
				names.append(name)
		if names:
			return max(set(names), key=names.count)

	def trigger_webhooks(self, replay):
		if self.is_fake:
			# Fake users should never have webhooks
			return

		webhooks = self.webhooks.filter(is_active=True, is_deleted=False)
		if webhooks.count():
			data = replay.serialize()
			for webhook in webhooks:
				webhook.trigger(data)


class AccountActivity(models.Model):
	id = models.BigAutoField(primary_key=True)
	action = models.CharField(max_length=255)
	remote_ip = models.GenericIPAddressField(default="0.0.0.0")
	ip_country = models.CharField(max_length=2, blank=True)
	user_agent = models.TextField(blank=True)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
		related_name="account_activity",
	)
	old_value = JSONField(blank=True, null=True)
	new_value = JSONField(blank=True, null=True)
	metadata = JSONField(blank=True, null=True)

	created = models.DateTimeField(auto_now_add=True, db_index=True)


class AccountDeleteRequest(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	reason = models.TextField(blank=True)
	delete_replay_data = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Delete request for %s" % (self.user)

	def process(self):
		if self.user.last_login > self.updated:
			# User logged back in since the request was filed. Request no longer valid.
			return
		if self.delete_replay_data:
			self.user.delete_replays()
		self.user.delete()


class AuthToken(models.Model):
	key = models.UUIDField("Key", primary_key=True, editable=False, default=uuid4)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
		related_name="auth_tokens", null=True, blank=True
	)
	created = models.DateTimeField("Created", auto_now_add=True)
	creation_apikey = models.ForeignKey(
		"api.APIKey", on_delete=models.CASCADE, related_name="tokens"
	)

	test_data = models.BooleanField(default=False)

	class Meta:
		db_table = "api_authtoken"

	def __str__(self):
		return str(self.key)

	def create_fake_user(self, save=True):
		"""
		Create a User instance with the same username as the key UUID.
		The user has the is_fake attribute set to True.
		"""
		user = User.objects.create(username=str(self.key), is_fake=True)
		self.user = user
		if save:
			self.save()
		return user


REGIONS = {
	BnetRegion.REGION_UNKNOWN: "Unknown region",
	BnetRegion.REGION_US: "North America (US)",
	BnetRegion.REGION_EU: "Europe (EU)",
	BnetRegion.REGION_KR: "Korea (KR)",
	BnetRegion.REGION_CN: "China (CN)",
	BnetRegion.REGION_TW: "South East Asia (SEA)",
}


class BlizzardAccount(models.Model):
	id = models.BigAutoField(primary_key=True)

	account_hi = models.BigIntegerField(
		"Account Hi",
		help_text="The region value from account hilo"
	)
	account_lo = models.BigIntegerField(
		"Account Lo",
		help_text="The account ID value from account hilo"
	)
	region = IntEnumField(enum=BnetRegion)
	battletag = models.CharField(max_length=64, blank=True)

	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
		null=True, blank=True, related_name="blizzard_accounts"
	)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "games_pegasusaccount"
		unique_together = ("account_hi", "account_lo")

	def __str__(self):
		region = REGIONS.get(self.region, "Dev. region")
		return "%s - %s" % (self.battletag, region)
