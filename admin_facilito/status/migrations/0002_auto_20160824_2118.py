# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
