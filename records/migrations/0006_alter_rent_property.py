# Generated by Django 4.0.1 on 2022-01-07 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_alter_rent_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='records.property'),
        ),
    ]
