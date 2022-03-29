# Generated by Django 4.0.3 on 2022-03-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_is_general_user_is_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='address_model',
            fields=[
                ('address_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('x', models.CharField(max_length=30)),
                ('y', models.CharField(max_length=30)),
                ('total_address', models.CharField(max_length=100)),
                ('detail_address', models.CharField(max_length=50)),
            ],
        ),
    ]