# Generated by Django 4.0.3 on 2022-03-18 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_rename_username_owner_ownername_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='phon_number',
            new_name='phone_number',
        ),
    ]
