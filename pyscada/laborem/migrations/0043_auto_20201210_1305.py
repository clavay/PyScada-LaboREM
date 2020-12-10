# Generated by Django 2.2.8 on 2020-12-10 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0042_auto_20201209_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboremrobotbase',
            name='requested_element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested_element', to='laborem.LaboremRobotElement'),
        ),
        migrations.AlterField(
            model_name='laboremrobotbase',
            name='element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='element', to='laborem.LaboremRobotElement'),
        ),
    ]