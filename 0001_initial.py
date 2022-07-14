# Generated by Django 4.0.5 on 2022-06-29 22:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Device ID')),
            ],
        ),
        migrations.CreateModel(
            name='MedicationNurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, null=True, verbose_name='Full Name')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-full_name'],
            },
        ),
        migrations.CreateModel(
            name='WorkstationNurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, null=True, verbose_name='Full Name')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-full_name'],
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name='Gender')),
                ('birth_date', models.DateField(null=True, verbose_name='Birth of Date')),
                ('phone_number_1', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number please', regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number 1')),
                ('phone_number_2', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number please', regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number 2')),
                ('country', models.CharField(max_length=20, null=True, verbose_name='Country')),
                ('city', models.CharField(max_length=60, null=True, verbose_name='City')),
                ('state', models.CharField(max_length=60, null=True, verbose_name='State')),
                ('address_1', models.CharField(max_length=200, null=True, verbose_name='Address line 1')),
                ('address_2', models.CharField(max_length=200, null=True, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, null=True, verbose_name='ZIP/ Postal code')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, null=True, verbose_name='Full Name')),
                ('start_date', models.DateField(auto_now_add=True, null=True, verbose_name='Arrival Date')),
                ('has_insurance', models.BooleanField(default=False, null=True, verbose_name='Insurance')),
                ('has_hypertension', models.BooleanField(default=False, null=True, verbose_name='Hypertension')),
                ('has_Diabetes', models.BooleanField(default=False, null=True, verbose_name='Diabetes')),
                ('has_Covid', models.BooleanField(default=False, null=True, verbose_name='Covid')),
                ('device', models.OneToOneField(null=True, on_delete=django.db.models.query.prefetch_related_objects, to='accounts.device')),
                ('m_nurse', models.ForeignKey(null=True, on_delete=django.db.models.query.prefetch_related_objects, to='accounts.medicationnurse')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('w_nurse', models.ForeignKey(null=True, on_delete=django.db.models.query.prefetch_related_objects, to='accounts.workstationnurse')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, null=True, verbose_name='Full Name')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-full_name'],
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, null=True, verbose_name='Full Name')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-full_name'],
            },
        ),
    ]
