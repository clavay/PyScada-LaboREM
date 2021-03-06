# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-24 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0028_auto_20190607_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboremExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('short_name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='', null=True, verbose_name='Description')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='laboremgroupinputpermission',
            name='laborem_experiences',
            field=models.ManyToManyField(blank=True, to='laborem.LaboremExperience'),
        ),
    ]
