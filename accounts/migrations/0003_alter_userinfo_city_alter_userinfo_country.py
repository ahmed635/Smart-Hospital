# Generated by Django 4.0.5 on 2022-07-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_patient_has_covid_alter_patient_has_diabetes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Country'),
        ),
    ]