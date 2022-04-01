# Generated by Django 4.0.3 on 2022-04-01 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_general_user_remove_user_is_general_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address_model',
            old_name='total_address',
            new_name='address_string',
        ),
        migrations.AddField(
            model_name='general_user',
            name='main_address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='authentication.address_model'),
        ),
        migrations.AddField(
            model_name='general_user',
            name='sub_address',
            field=models.CharField(default='', max_length=30),
        ),
    ]
