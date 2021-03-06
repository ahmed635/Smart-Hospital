# Generated by Django 4.0.5 on 2022-07-08 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_patient_user_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='has_Covid',
            field=models.CharField(default='', max_length=150, null=True, verbose_name='Covid'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_Diabetes',
            field=models.CharField(default='', max_length=150, null=True, verbose_name='Diabetes'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_hypertension',
            field=models.CharField(default='', max_length=150, null=True, verbose_name='Hypertension'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_insurance',
            field=models.CharField(default='', max_length=150, null=True, verbose_name='Insurance'),
        ),
    ]
