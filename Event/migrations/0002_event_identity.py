# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-02 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='identity',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
