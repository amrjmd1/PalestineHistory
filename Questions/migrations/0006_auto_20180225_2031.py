# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-25 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0005_auto_20180225_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
