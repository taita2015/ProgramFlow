# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0022_auto_20170414_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='last_time',
            new_name='last_edit_time',
        ),
        migrations.AddField(
            model_name='thread',
            name='last_reply_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]