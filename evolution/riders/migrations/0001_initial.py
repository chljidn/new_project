# Generated by Django 4.0.3 on 2022-03-30 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0011_general_user_remove_user_is_general_and_more'),
        ('order', '0012_alter_basket_user_id_alter_order_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='rider',
            fields=[
                ('rider_id', models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='rider_order',
            fields=[
                ('order_id', models.OneToOneField(db_column='order', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='order.order')),
                ('rider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riders.rider')),
            ],
        ),
    ]