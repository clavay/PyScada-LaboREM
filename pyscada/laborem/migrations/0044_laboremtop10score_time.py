# Generated by Django 2.2.8 on 2021-02-09 08:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0043_auto_20201210_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboremtop10score',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
