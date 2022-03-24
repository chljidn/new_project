# Generated by Django 4.0.3 on 2022-03-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_general',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
    ]