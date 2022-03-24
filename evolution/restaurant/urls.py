from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views as res_views

name = 'restarutant'
router = DefaultRouter()
router.register('res', res_views.restaurant_view, basename='restaurant')
router.register('auth', res_views.owner_auth_view, basename='owner_auth')

urlpatterns = [
    path('', include(router.urls))
]