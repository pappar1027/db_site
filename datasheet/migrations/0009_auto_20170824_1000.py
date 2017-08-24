# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 10:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0008_auto_20170824_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='calls_or_puts',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='option',
            name='last_edit',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 10, 0, 55, 465589, tzinfo=utc), verbose_name='last edit date'),
        ),
    ]
