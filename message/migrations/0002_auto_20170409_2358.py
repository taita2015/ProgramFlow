# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 15:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemtousermessage',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='systemtousermessage',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemtousermessage',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='systemtousermessage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]