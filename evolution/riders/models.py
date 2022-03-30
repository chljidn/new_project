from django.db import models
from authentication.models import User
from order.models import order

class rider(models.Model):
    rider_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, db_column="user")

class rider_order(models.Model):
    order_id = models.OneToOneField(order, primary_key=True, on_delete=models.CASCADE, db_column="order")
    rider_id = models.ForeignKey(rider, on_delete=models.CASCADE)
