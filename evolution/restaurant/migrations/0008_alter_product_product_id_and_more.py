# Generated by Django 4.0.3 on 2022-03-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_restaurant_owner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]