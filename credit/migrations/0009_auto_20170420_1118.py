# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0008_auto_20170420_1115'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreditDefault',
            new_name='CreditStatus',
        ),
    ]