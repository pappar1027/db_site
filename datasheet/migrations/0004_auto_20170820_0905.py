# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 09:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0003_auto_20170820_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='last_edit',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 20, 9, 5, 56, 702550, tzinfo=utc), verbose_name='last edit date'),
        ),
    ]
