# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worm_strains', '0011_auto_20160309_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wormstrain',
            name='id',
            field=models.CharField(help_text=b'After saving, this field cannot be changed through the admin interface. If you need to change it, please do so in the database directly. You will need to edit the worm strain pointers for all corresponding worm strain lines, too.', max_length=30, primary_key=True, serialize=False),
        ),
    ]
