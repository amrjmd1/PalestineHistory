# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-10 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_loginattempts_useragents'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginattempts',
            name='manage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useragents',
            name='manage',
            field=models.BooleanField(default=False),
        ),
    ]
