# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-22 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_add_profile_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='securityanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.SecurityQuestion'),
        ),
        migrations.AddField(
            model_name='securityanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='security_question_answers',
            field=models.ManyToManyField(through='profiles.SecurityAnswer', to='profiles.SecurityQuestion'),
        ),
    ]
