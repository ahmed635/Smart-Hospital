# Generated by Django 4.0.5 on 2022-07-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_message_full_name_message_time_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True, verbose_name='Time'),
        ),
    ]
