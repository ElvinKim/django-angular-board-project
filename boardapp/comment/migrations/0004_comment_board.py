# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_remove_board_comment'),
        ('comment', '0003_remove_comment_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posting_id', to='board.Board'),
        ),
    ]