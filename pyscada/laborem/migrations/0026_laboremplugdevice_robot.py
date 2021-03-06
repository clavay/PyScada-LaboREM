# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-04 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0007_auto_20171219_1327'),
        ('laborem', '0025_auto_20181121_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboremplugdevice',
            name='robot',
            field=models.ForeignKey(blank=True, help_text='If the PCB Plug is modifiable with the robot choose the Robot device. If not let it blank', null=True, on_delete=django.db.models.deletion.CASCADE, to='visa.VISADevice'),
        ),
    ]
