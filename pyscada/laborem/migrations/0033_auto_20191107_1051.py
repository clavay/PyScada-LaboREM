# Generated by Django 2.2.6 on 2019-11-07 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laborem', '0032_auto_20191004_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug1',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug10',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug11',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug12',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug13',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug14',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug15',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug16',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug2',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug3',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug4',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug5',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug6',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug7',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug8',
        ),
        migrations.RemoveField(
            model_name='laboremmotherboarddevice',
            name='plug9',
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug1', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug10', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug11',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug11', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug12',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug12', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug13',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug13', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug14',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug14', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug15',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug15', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug16',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug16', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug2', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug3', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug4', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug5', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug6', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug7', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug8', to='laborem.LaboremPlugDevice'),
        ),
        migrations.AddField(
            model_name='laboremmotherboardioconfig',
            name='plug9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobo_plug9', to='laborem.LaboremPlugDevice'),
        ),
    ]
