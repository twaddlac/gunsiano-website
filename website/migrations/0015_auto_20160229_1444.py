# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20160229_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='pmid',
            field=models.PositiveIntegerField(default=123, verbose_name=b'PMID'),
            preserve_default=False,
        ),
    ]
