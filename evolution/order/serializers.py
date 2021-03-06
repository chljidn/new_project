from rest_framework import serializers
from authentication.serializers import user_serializer
from restaurant.serializers import product_serializer
from order.models import basket, order, order_detail


class basket_serializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField()
    product_id = serializers.StringRelatedField()
    class Meta:
        model = basket
        fields = ('basket_id', 'username', 'product_id', 'count')

class order_serializer(serializers.ModelSerializer):
    order_detail_set = serializers.StringRelatedField
    class Meta:
        model = order
        fields = ('order_id', 'order_time', 'prediction_time')