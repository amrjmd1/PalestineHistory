# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-01 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('poster', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]