from rest_framework import serializers
from riders.models import rider, rider_order
from order.serializers import order_serializer

class rider_order_serializer(serializers.ModelSerializer):
    order = order_serializer(read_only=True, many=True)
    class Meta:
        model = rider_order
        fields = ("order", )