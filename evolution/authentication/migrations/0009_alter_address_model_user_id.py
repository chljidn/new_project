# Generated by Django 4.0.3 on 2022-03-25 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_address_model_user_id_alter_address_model_address_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address_model',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
