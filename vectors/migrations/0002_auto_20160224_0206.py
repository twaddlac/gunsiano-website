# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vectors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vector',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vector',
            name='parent_vector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vectors.Vector'),
        ),
    ]
