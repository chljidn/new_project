from rest_framework import serializers
from authentication.models import User
from restaurant.models import restaurant, product

class restaurant_serializer(serializers.ModelSerializer):
    class Meta:
        model = restaurant
        fields = '__all__'

class owner_serializer(serializers.ModelSerializer):
    # restaurant_set = restaurant_serializer
    restaurant_set = serializers.StringRelatedField(many=True)
    # restaurant_set = restaurant_serializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'birth', 'sex', 'restaurant_set')

class product_serializer(serializers.ModelSerializer):
    restaurant_id = serializers.StringRelatedField()
    class Meta:
        model = product
        fields = ('product_id', 'restaurant_id', 'product_name', 'price', 'category', 'image', 'content')
