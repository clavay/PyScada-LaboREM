# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-09 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0011_auto_20180906_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboremrobotbase',
            name='element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='laborem.LaboremRobotElement'),
        ),
    ]
