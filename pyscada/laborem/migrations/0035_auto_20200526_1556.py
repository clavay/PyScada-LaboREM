# Generated by Django 2.2.8 on 2020-05-26 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0034_auto_20191107_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboremtop10',
            name='score1',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='laboremtop10',
            name='score2',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='laboremtop10',
            name='score3',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='laboremtop10',
            name='score4',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='laboremtop10',
            name='robot_base1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='robot_base1', to='laborem.LaboremRobotElement', verbose_name='Robot base vert'),
        ),
        migrations.AlterField(
            model_name='laboremtop10',
            name='robot_base2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='robot_base2', to='laborem.LaboremRobotElement', verbose_name='Robot base rouge'),
        ),
    ]
