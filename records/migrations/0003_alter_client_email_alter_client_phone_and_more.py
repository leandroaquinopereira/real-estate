# Generated by Django 4.0.1 on 2022-01-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_alter_property_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='property',
            name='value',
            field=models.CharField(max_length=15),
        ),
    ]
