# Generated by Django 2.2.8 on 2020-11-30 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0040_auto_20201126_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboremtop10',
            name='sub_plug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='laborem.LaboremSubPlugDevice'),
        ),
    ]
