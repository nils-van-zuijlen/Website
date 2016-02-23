# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('asso', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asso',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='asso',
            name='members',
        ),
        migrations.AddField(
            model_name='asso',
            name='admins_group',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asso_admin_set', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='asso',
            name='members_group',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asso_set', to='auth.Group'),
        ),
    ]