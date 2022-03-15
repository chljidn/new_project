from django.urls import include, path
from rest_framework.routers import DefaultRouter
from order import views as order_views

app_name = "order"

router= DefaultRouter()
router.register('basket', order_views.basket, basename='basket')
router.register('my_order', order_views.order_view, basename='my_order')

urlpatterns = [
    path('', include(router.urls))
]