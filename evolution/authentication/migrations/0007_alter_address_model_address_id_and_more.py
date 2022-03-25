# Generated by Django 4.0.3 on 2022-03-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_address_model_detail_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address_model',
            name='address_id',
            field=models.IntegerField(auto_created=True, db_column='address_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='address_model',
            name='total_address',
            field=models.CharField(db_column='total_address', max_length=100),
        ),
        migrations.AlterField(
            model_name='address_model',
            name='x',
            field=models.CharField(db_column='x', max_length=30),
        ),
        migrations.AlterField(
            model_name='address_model',
            name='y',
            field=models.CharField(db_column='y', max_length=30),
        ),
        migrations.AlterModelTable(
            name='address_model',
            table='address',
        ),
    ]
