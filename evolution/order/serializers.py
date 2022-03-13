from rest_framework import serializers
from authentication.serializers import user_serializer
from restaurant.serializers import product_serializer
from order.models import basket


class basket_serializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField()
    product_id = serializers.StringRelatedField()
    class Meta:
        model = basket
        fields = ('basket_id', 'username', 'product_id', 'count')