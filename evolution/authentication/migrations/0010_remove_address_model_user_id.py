# Generated by Django 4.0.3 on 2022-03-25 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_address_model_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address_model',
            name='user_id',
        ),
    ]