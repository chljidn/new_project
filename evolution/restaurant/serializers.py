from rest_framework import serializers
from authentication.models import User
from restaurant.models import restaurant, product, owner
from authentication.serializers import user_serializer

class restaurant_serializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant
        fields = '__all__'

class owner_serializer(serializers.ModelSerializer):
    user = user_serializer(read_only=True)
    restaurant_set = serializers.StringRelatedField(many=True)
    class Meta:
        model = owner
        fields = ('user', 'restaurant_set')


class product_serializer(serializers.ModelSerializer):
    restaurant_id = serializers.StringRelatedField()
    class Meta:
        model = product
        fields = ('product_id', 'restaurant_id', 'product_name', 'price', 'category', 'image', 'content')
