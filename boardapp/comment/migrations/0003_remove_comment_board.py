# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 01:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='board',
        ),
    ]
