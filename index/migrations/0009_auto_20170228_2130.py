# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20170228_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=index.models.upload_to),
        ),
    ]
