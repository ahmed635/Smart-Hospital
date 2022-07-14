# Generated by Django 4.0.5 on 2022-07-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='has_Covid',
            field=models.BooleanField(null=True, verbose_name='Covid'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_Diabetes',
            field=models.BooleanField(null=True, verbose_name='Diabetes'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_hypertension',
            field=models.BooleanField(null=True, verbose_name='Hypertension'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_insurance',
            field=models.BooleanField(null=True, verbose_name='Insurance'),
        ),
    ]
