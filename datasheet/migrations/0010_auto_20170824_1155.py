# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 11:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('datasheet', '0009_auto_20170824_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='id',
        ),
        migrations.AlterField(
            model_name='option',
            name='contract_name',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='option',
            name='last_edit',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 11, 55, 7, 439885, tzinfo=utc), verbose_name='last edit date'),
        ),
    ]