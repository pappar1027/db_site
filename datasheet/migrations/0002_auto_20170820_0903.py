# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 09:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='last_edit',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 20, 9, 3, 28, 989439), verbose_name='last edit date'),
        ),
        migrations.AlterField(
            model_name='option',
            name='last_trade_date',
            field=models.DateTimeField(verbose_name='last trade date'),
        ),
    ]
