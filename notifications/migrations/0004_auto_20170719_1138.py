# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20170719_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ('-create_date',)},
        ),
    ]
