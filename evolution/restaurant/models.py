from django.db import models
from authentication.models import User
# 업체 소유주
class owner(models.Model):
    ownername = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

# 업체 주소
# class restaurant_address(models.Model):
#     pass

# 업체
class restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(owner, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=100)
    # restaurant_address = models.ForeignKey(restaurant_address, on_delete=models.PROTECT)
    phon_number = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.restaurant_name

# 상품
class product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE, db_column="restaurant_id")
    product_name = models.TextField(default="")
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    image = models.IntegerField()
    content = models.TextField(default="")

    def __str__(self):
        return self.product_name


