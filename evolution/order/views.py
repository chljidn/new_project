from django.shortcuts import render
from order.models import basket, order
from rest_framework import viewsets

# Create your views here.
# 장바구니
class basket(viewsets.ViewSet):
    queryset = basket.objects.all()
    def list(self):

        pass
    def update(self, request):
        pass
    def destroy(self, request):
        pass