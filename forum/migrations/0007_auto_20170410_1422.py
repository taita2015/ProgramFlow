# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20170410_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['order'], 'verbose_name': '父帖子类型', 'verbose_name_plural': '父帖子类型'},
        ),
    ]