# Generated by Django 4.0.5 on 2022-07-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medication_nurse', '0004_alter_tasklist_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='delivery_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='delivery_time',
            field=models.TimeField(auto_now_add=True, null=True, verbose_name='Time'),
        ),
    ]
