# Generated by Django 4.0.3 on 2022-03-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_rename_phon_number_restaurant_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
