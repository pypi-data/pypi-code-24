# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, help_text='This value is set automatically.', max_length=10, unique=True, verbose_name='Bill number')),
                ('isPaid', models.BooleanField(default=False, help_text='Check this value when bill is paid', verbose_name='Bill is paid ?')),
                ('billing_date', models.DateField(auto_now_add=True, help_text='This value is set automatically.', verbose_name='Date')),
                ('amount', models.FloatField(blank=True, default=0, help_text='The amount is computed automatically.', verbose_name='Bill total amount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Coworker')),
            ],
            options={
                'verbose_name': 'Bill',
            },
        ),
        migrations.CreateModel(
            name='BillLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(default=1, verbose_name='Quantity')),
                ('total', models.FloatField(blank=True, help_text='This value is computed automatically', verbose_name='Total')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billjobs.Bill')),
            ],
            options={
                'verbose_name_plural': 'Bill Lines',
                'verbose_name': 'Bill Line',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=5, verbose_name='Reference')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Service',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_address', models.TextField(max_length=1024, verbose_name='Billing Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Profiles',
                'verbose_name': 'User Profile',
            },
        ),
        migrations.AddField(
            model_name='billline',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billjobs.Service'),
        ),
    ]
