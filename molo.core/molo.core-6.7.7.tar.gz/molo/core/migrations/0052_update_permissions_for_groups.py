# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-23 12:29
# flake8: noqa: E303, F841
from __future__ import unicode_literals

from django.db import migrations
from django.core.management.sql import emit_post_migrate_signal



def update_permissions_for_group(apps, schema_editor):
    '''
    Update permissions for some users.

    Give bulk-delete permissions to moderators.
    Give edit permission to moderators and editors in order
    to display 'Main' page in the explorer.
    '''
    db_alias = schema_editor.connection.alias
    try:
        # Django 1.9
        emit_post_migrate_signal(2, False, db_alias)
    except TypeError:
        # Django < 1.9
        try:
            # Django 1.8
            emit_post_migrate_signal(2, False, 'default', db_alias)
        except TypeError:  # Django < 1.8
            emit_post_migrate_signal([], 2, False, 'default', db_alias)

    Group = apps.get_model('auth.Group')
    Permission = apps.get_model('auth.Permission')
    GroupPagePermission = apps.get_model('wagtailcore.GroupPagePermission')
    SectionIndexPage = apps.get_model('core.SectionIndexPage')
    MainPage = apps.get_model('core.Main')

    moderator_group = Group.objects.filter(name='Moderators').first()
    editor_group = Group.objects.filter(name='Editors').first()

    if moderator_group:
        sections = SectionIndexPage.objects.first()
        GroupPagePermission.objects.get_or_create(
            group_id=moderator_group.id,
            page_id=sections.id,
            permission_type='bulk_delete'
        )

        main = MainPage.objects.first()
        GroupPagePermission.objects.get_or_create(
            group_id=moderator_group.id,
            page_id=main.id,
            permission_type='edit'
        )

    if editor_group:
        main = MainPage.objects.first()
        GroupPagePermission.objects.get_or_create(
            group_id=editor_group.id,
            page_id=main.id,
            permission_type='edit'
        )


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0051_remove_user_permission_for_moderator_group'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailadmin', '0001_create_admin_access_permissions'),
        ('wagtailusers', '0005_make_related_name_wagtail_specific'),
        ('sites', '0002_alter_domain_unique'),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.RunPython(
            update_permissions_for_group),
    ]
