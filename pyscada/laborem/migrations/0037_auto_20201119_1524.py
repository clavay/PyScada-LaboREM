# Generated by Django 2.2.8 on 2020-11-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0036_auto_20201119_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='C1',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='C1 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='C2',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='C2 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='C3',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='C3 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='C4',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='C4 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='C5',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='C5 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='C6',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='C6 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='C7',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='C7 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='C8',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='C8 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='V1',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='V1 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='V2',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='V2 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='V3',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='V3 connector'),
        ),
        migrations.AlterField(
            model_name='laboremmotherboardioconfig',
            name='V4',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'switch1'), (2, 'switch2'), (3, 'switch3'), (4, 'switch4'), (10, 'MDO1'), (11, 'MDO2'), (12, 'MDO3'), (13, 'MDO4'), (20, 'AFG1'), (21, 'AFG2'), (30, 'DMM_High'), (31, 'DMM_Low'), (40, 'DC1'), (41, 'DC2')], default=0, help_text='V4 connector'),
        ),
    ]
