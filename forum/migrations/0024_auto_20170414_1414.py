# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 06:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0023_auto_20170414_1104'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSummer',
            new_name='UserThreadStatus',
        ),
    ]
