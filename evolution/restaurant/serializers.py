from rest_framework import serializers
from restaurant.models import restaurant, product, owner

class owner_serializer(serializers.ModelSerializer):
    class Meta:
        model = owner
        fields = ('username', 'phone_number', 'email')

class restaurant_serializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant
        fields = ('restaurant_id')

class product_serializer(serializers.ModelSerializer):
    restaurant_id = serializers.StringRelatedField()
    class Meta:
        model = product
        fields = ('product_id', 'restaurant_id', 'product_name', 'price', 'category', 'image', 'content')
