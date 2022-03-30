from django.db import models
from authentication.models import User

class owner(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, db_column="user")


# 업체 주소
# class restaurant_address(models.Model):

# 업체
class restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='owner_id')
    restaurant_name = models.CharField(max_length=100)
    # restaurant_address = models.ForeignKey(restaurant_address, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.restaurant_name

# 상품
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE, db_column="restaurant_id")
    product_name = models.TextField(default="")
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    image = models.IntegerField(null=True)
    content = models.TextField(default="")

    def __str__(self):
        return self.product_name


