# Generated by Django 4.0.3 on 2022-03-18 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_product_restaurant_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='username',
            new_name='ownername',
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]