# Generated by Django 4.0.1 on 2022-01-10 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Kitnet', 'Kitnet'), ('House', 'House')], max_length=10),
        ),
    ]
