# Generated by Django 4.0.3 on 2022-03-30 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_basket_user_id_alter_order_user_id'),
        ('riders', '0002_delete_rider_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='rider_order',
            fields=[
                ('order_id', models.OneToOneField(db_column='order', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='order.order')),
                ('rider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riders.rider')),
            ],
        ),
    ]
