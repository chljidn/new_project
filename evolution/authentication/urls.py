from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication import views as auth_view

app_name='authentication'

router = DefaultRouter()
router.register(r'signup', auth_view.user_auth, basename='signup')

urlpatterns = [
    path('', include(router.urls))
]