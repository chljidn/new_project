from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication import views as auth_view

app_name='authentication'

router = DefaultRouter()
router.register(r'user', auth_view.user_auth, basename='user')

urlpatterns = [
    path('', include(router.urls))
]