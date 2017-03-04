# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 13:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_auto_20170303_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='TAG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='thread',
            name='name',
        ),
        migrations.AddField(
            model_name='thread',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='thread',
            name='create_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='create_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='thread',
            name='last_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='tittle',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]