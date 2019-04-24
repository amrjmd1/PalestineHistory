# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-22 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0006_auto_20180722_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=60, unique=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='identity',
            field=models.CharField(max_length=15),
        ),
    ]