# Generated by Django 2.2.6 on 2019-10-04 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0031_laboremmotherboardioconfig_mdo2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboremexperience',
            name='page',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hmi.Page'),
        ),
        migrations.AlterField(
            model_name='laboremgroupinputpermission',
            name='hmi_group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='laboremgroupinputpermission',
            name='move_robot',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='laboremgroupinputpermission',
            name='top10_answer',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='afg1',
            field=models.ForeignKey(blank=True, help_text='Function Generator', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='afg1', to='pyscada.Device'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='dcps1',
            field=models.ForeignKey(blank=True, help_text='DC Power Supply', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dcps1', to='pyscada.Device'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='dmm1',
            field=models.ForeignKey(blank=True, help_text='Multimeter', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mm1', to='pyscada.Device'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='mdo1',
            field=models.ForeignKey(blank=True, help_text='Oscilloscope', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='osc1', to='pyscada.Device'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='mdo2',
            field=models.ForeignKey(blank=True, help_text='Oscilloscope', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='osc2', to='pyscada.Device'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='pin1',
            field=models.OneToOneField(blank=True, help_text='A0 connector', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobo_pin1', to='gpio.GPIOVariable'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='pin2',
            field=models.OneToOneField(blank=True, help_text='A1 connector', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobo_pin2', to='gpio.GPIOVariable'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='pin3',
            field=models.OneToOneField(blank=True, help_text='A2 connector', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobo_pin3', to='gpio.GPIOVariable'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='pin4',
            field=models.OneToOneField(blank=True, help_text='A3 connector', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobo_pin4', to='gpio.GPIOVariable'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='pin5',
            field=models.OneToOneField(blank=True, help_text='Relay', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobo_pin5', to='gpio.GPIOVariable'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='pin6',
            field=models.OneToOneField(blank=True, help_text='Ground', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobo_pin6', to='gpio.GPIOVariable'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='robot1',
            field=models.ForeignKey(blank=True, help_text='Robot Arm', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='robot1', to='pyscada.Device'),
        ),
        migrations.AlterField(
            model_name='laboremplugdevice',
            name='motherboardIOConfig',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='laborem.LaboremMotherboardIOConfig'),
        ),
        migrations.AlterField(
            model_name='laboremplugdevice',
            name='robot',
            field=models.ForeignKey(blank=True, help_text='If the PCB Plug is modifiable with the robot choose the Robot device. If not let it blank', null=True, on_delete=django.db.models.deletion.SET_NULL, to='visa.VISADevice'),
        ),
        migrations.AlterField(
            model_name='laboremrobotbase',
            name='element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='laborem.LaboremRobotElement'),
        ),
        migrations.AlterField(
            model_name='laboremrobotelement',
            name='robot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visa.VISADevice'),
        ),
        migrations.AlterField(
            model_name='laboremtop10',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='laboremtop10',
            name='page',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hmi.Page'),
        ),
        migrations.AlterField(
            model_name='laboremtop10',
            name='plug',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='laborem.LaboremPlugDevice'),
        ),
        migrations.AlterField(
            model_name='laboremtop10',
            name='robot_base1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='robot_base1', to='laborem.LaboremRobotElement'),
        ),
        migrations.AlterField(
            model_name='laboremtop10',
            name='robot_base2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='robot_base2', to='laborem.LaboremRobotElement'),
        ),
        migrations.AlterField(
            model_name='laboremtop10ranking',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='laboremtop10ranking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='laboremtop10score',
            name='TOP10QA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='laborem.LaboremTOP10'),
        ),
        migrations.AlterField(
            model_name='laboremtop10score',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='laboremtop10score',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='laboremuser',
            name='laborem_group_input',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='laborem.LaboremGroupInputPermission'),
        ),
        migrations.AlterField(
            model_name='laboremuser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
