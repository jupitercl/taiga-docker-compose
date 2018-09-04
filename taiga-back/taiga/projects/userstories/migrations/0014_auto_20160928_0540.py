# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-28 05:40
from __future__ import unicode_literals

from django.db import migrations, models
import taiga.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0013_auto_20160722_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='backlog_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='backlog order'),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='kanban_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='kanban order'),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='sprint_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='sprint order'),
        ),
    ]
