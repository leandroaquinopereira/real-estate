# Generated by Django 4.0.1 on 2022-01-10 02:23

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=35)),
                ('cpf', cpf_field.models.CPFField(max_length=14, unique=True, verbose_name='cpf')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Apartment', 'Apartment'), ('kitnet', 'kitnet'), ('House', 'House')], max_length=10)),
                ('address', models.CharField(max_length=150, unique=True)),
                ('value', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('rented', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='records.client')),
                ('property', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='records.property')),
            ],
            options={
                'verbose_name': 'Rent',
                'verbose_name_plural': 'Rents',
            },
        ),
    ]
