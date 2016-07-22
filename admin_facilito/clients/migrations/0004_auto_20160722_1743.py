# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_socialnetwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='job',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='twitter',
            field=models.URLField(blank=True),
        ),
    ]
