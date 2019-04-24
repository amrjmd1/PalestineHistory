# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-22 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0005_auto_20180720_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]