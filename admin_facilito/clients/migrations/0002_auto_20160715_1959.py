# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bio',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='job',
            field=models.CharField(default='', max_length=50),
        ),
    ]
