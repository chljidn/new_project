from django.urls import path, include
from rest_framework.routers import DefaultRouter
from riders.views import delivery, rider_auth_view

name = "riders"

router = DefaultRouter()
router.register('rider', rider_auth_view, basename='rider')

urlpatterns = [
    path('delivery', delivery.as_view()),
    path('', include(router.urls))
]