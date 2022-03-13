from django.db import models
from authentication.models import User
from restaurant.models import product
# Create your models here.

class basket(models.Model):
    basket_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    count = models.IntegerField()

class order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    prediction_time = models.DateTimeField()

class order_detail(models.Model):
    order_detail_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.PROTECT)
    count = models.IntegerField()