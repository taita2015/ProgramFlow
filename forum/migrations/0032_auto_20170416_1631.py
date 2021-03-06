# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 08:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0031_auto_20170416_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='userthreadstatus',
            name='collected',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userthreadstatus',
            name='disliked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userthreadstatus',
            name='liked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userthreadstatus',
            name='reply_open',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userthreadstatus',
            name='thread_open',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userthreadstatus',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
