# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pylucid_todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='pylucid_todo_todoplugin', serialize=False, to='cms.CMSPlugin'),
        ),
    ]
