# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-21 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0042_auto_20180604_1240'),
        ('laborem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedLaboremMotherboardDevice',
            fields=[
            ],
            options={
                'verbose_name': 'Laborem Motherboard Device',
                'proxy': True,
                'verbose_name_plural': 'Laborem Motherboard Devices',
                'indexes': [],
            },
            bases=('pyscada.device',),
        ),
    ]
