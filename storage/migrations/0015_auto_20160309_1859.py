# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0014_auto_20160309_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containertype',
            name='slots_horizontal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='containertype',
            name='slots_vertical',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
