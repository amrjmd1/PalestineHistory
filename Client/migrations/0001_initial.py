# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-25 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, unique=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('grand_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_manager', models.BooleanField(default=False)),
            ],
        ),
    ]
