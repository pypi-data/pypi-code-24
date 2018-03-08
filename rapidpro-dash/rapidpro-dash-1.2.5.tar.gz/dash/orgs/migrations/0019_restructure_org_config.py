# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 08:24
from __future__ import unicode_literals

import json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0018_auto_20170301_0914'),
    ]

    def migrate_api_token_and_common_org_config(apps, schema_editor):
        Org = apps.get_model("orgs", "Org")
        orgs = Org.objects.all()

        for org in orgs:
            if not org.config:
                old_config = dict()
            else:
                old_config = json.loads(self.config)

            if "common" in old_config and "rapidpro" in old_config:
                print("Skipped org(%d), it looks like already migrated" % org.id)
                continue

            new_config = {"common": old_config, "rapidro": {"api_token": org.api_token}}
            self.config = json.dumps(new_config)
            self.save()

    def noop(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(migrate_api_token_and_common_org_config, noop)
    ]
