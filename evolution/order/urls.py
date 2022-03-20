from django.urls import include, path
from rest_framework.routers import DefaultRouter
from order import views as order_views

app_name = "order"

router= DefaultRouter()
router.register('basket', order_views.basket, basename='basket')
urlpatterns = [
    path('my_order/', order_views.order_view.as_view()),
    # path('my_order/<int:pk>/', order_views.order_view.as_view()),
    path('', include(router.urls))
]