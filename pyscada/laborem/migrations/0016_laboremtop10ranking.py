# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-18 15:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laborem', '0015_auto_20181018_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboremTOP10Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-score'],
                'verbose_name': 'Laborem TOP10 Ranking',
                'verbose_name_plural': 'Laborem TOP10 Ranking',
            },
        ),
    ]
