from restaurant.models import restaurant
from django_filters import rest_framework as filters

class restaurant_filter(filters.FilterSet):
    class Meta:
        model = restaurant
        fields = ['restaurant_name', 'category']