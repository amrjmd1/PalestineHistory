# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-23 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0009_auto_20180723_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useragents',
            name='user',
            field=models.CharField(max_length=60),
        ),
    ]