# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0012_auto_20160303_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='horizontal_position',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='container',
            name='vertical_position',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
