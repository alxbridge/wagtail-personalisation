# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20170531_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='canonical_page',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='is_segmented',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='segment',
        ),
        migrations.RemoveField(
            model_name='specialpage',
            name='canonical_page',
        ),
        migrations.RemoveField(
            model_name='specialpage',
            name='is_segmented',
        ),
        migrations.RemoveField(
            model_name='specialpage',
            name='segment',
        ),
    ]
