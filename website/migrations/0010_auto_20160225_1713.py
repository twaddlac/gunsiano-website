# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20160225_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='pmcid',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
    ]