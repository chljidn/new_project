from django.urls import include, path
from rest_framework.routers import DefaultRouter
from order import views as order_views

app_name = "order"

router= DefaultRouter()
router.register('basket', order_views.basket, basename='basket')

urlpatterns = [
    path('', include(router.urls))
]