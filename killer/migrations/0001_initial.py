# -*- coding: utf-8 -*-
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
            name='Killer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_start_date', models.DateTimeField()),
                ('registration_end_date', models.DateTimeField()),
                ('game_start_date', models.DateTimeField()),
                ('game_end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dead', models.BooleanField(default=False)),
                ('action', models.TextField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='killer.Killer')),
                ('killing', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='killed_by', to='killer.Participant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
