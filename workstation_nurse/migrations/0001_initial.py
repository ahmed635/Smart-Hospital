# Generated by Django 4.0.5 on 2022-06-29 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoursOfWorkstationNurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_date', models.DateField(verbose_name='Date')),
                ('total_hours', models.CharField(max_length=30, null=True, verbose_name='Total Hours')),
                ('w_nurse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.workstationnurse')),
            ],
            options={
                'ordering': ['-day_date'],
            },
        ),
    ]
