# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocols', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='author',
            field=models.ForeignKey(blank=True, help_text=b'If none selected, will default to logged in user.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
