# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='user',
        ),
        migrations.AddField(
            model_name='board',
            name='member_id',
            field=models.IntegerField(default=0),
        ),
    ]
