# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-26 09:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0020_auto_20181026_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboremuser',
            name='connection_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='laboremuser',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
