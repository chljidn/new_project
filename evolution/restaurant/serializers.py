from rest_framework import serializers
from restaurant.models import restaurant, product


class restaurant_serializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant
        fields = ()

class product_serializer(serializers.ModelSerializer):
    restaurant_id = serializers.StringRelatedField(restaurant_serializer)
    class Meta:
        model = product
        fields = ('product_id', 'restaurant_id', 'product_name', 'price', 'category', 'image', 'content')
