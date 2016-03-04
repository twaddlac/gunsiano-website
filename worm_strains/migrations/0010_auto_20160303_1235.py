# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worm_strains', '0009_auto_20160302_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wormstrain',
            name='genotype',
            field=models.CharField(help_text=b'If a precise genotype is unavailable or not easily written, put something meaningful about what the strain is -- e.g. "suppressor of X". If no information is available, put "n/a".', max_length=500),
        ),
        migrations.AlterField(
            model_name='wormstrain',
            name='on_wormbase',
            field=models.BooleanField(default=False, help_text=b'Check this if the strain is on WormBase. In this case, aside from genotype and important remarks such as temperature sensitivitiy, there is no need to fill in the fields which can be found on WormBase.'),
        ),
        migrations.AlterField(
            model_name='wormstrainline',
            name='created_internally',
            field=models.BooleanField(default=False, help_text=b'Check this if the line was created in our lab. In this case, the fields about receiving the strain will typically be blank.'),
        ),
    ]