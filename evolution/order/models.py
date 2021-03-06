from django.db import models
from authentication.models import general_user
from restaurant.models import product
from django.utils import timezone

class basket(models.Model):
    basket_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(general_user, on_delete=models.CASCADE, db_column='username')
    product_id = models.ForeignKey(product, on_delete=models.CASCADE, db_column="product_id")
    count = models.IntegerField()

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(general_user, on_delete=models.CASCADE, db_column="user_id")
    order_time = models.DateTimeField()
    prediction_time = models.DateTimeField()

class order_detail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE, db_column="order_id")
    product_id = models.ForeignKey(product, on_delete=models.PROTECT, db_column="product_id")
    count = models.IntegerField()