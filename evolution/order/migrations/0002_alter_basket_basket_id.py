# Generated by Django 4.0.3 on 2022-03-13 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='basket_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
