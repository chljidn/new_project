from django.shortcuts import render
from order.models import basket, order
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
# 장바구니
class basket(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = basket.objects.all()
    def filter_queryset(self, request, queryset):
        return queryset.filter(username=request.user)
    #
    def retrieve(self, request, pk=None):
        if request.user.is_authenticated:
            basket_list = self.filter_queryset(request, self.queryset)
            # serializer =

    def update(self, request):
        pass
    def destroy(self, request):
        pass