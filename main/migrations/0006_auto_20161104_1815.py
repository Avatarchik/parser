# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_odds'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='odds',
            options={'managed': False},
        ),
    ]
