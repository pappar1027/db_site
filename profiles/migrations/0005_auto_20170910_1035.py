# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20170825_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=120)),
                ('datasheet_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Datasheet_app')),
            ],
            options={
                'ordering': ('datasheet_name',),
            },
        ),
        migrations.RemoveField(
            model_name='data_admin',
            name='admin_email',
        ),
        migrations.AddField(
            model_name='data_admin',
            name='admin_name',
            field=models.CharField(default='', max_length=120),
        ),
    ]
