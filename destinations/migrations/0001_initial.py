# Generated by Django 5.0.3 on 2024-04-01 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('pricePerNight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spotsAvailable', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='destinations.user')),
                ('company_name', models.CharField(max_length=100)),
                ('license_number', models.CharField(max_length=20)),
            ],
            bases=('destinations.user',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='destinations.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
            bases=('destinations.user',),
        ),
    ]
