# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-23 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0008_auto_20180722_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifyemail',
            name='random_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]