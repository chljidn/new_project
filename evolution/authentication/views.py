from django.shortcuts import render
from rest_framework import viewsets
from authentication.models import User
from authentication.serializers import user_serializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import sys
from django.contrib.auth import authenticate, login

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class sign_up(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer

    def create(self, request):
        user_id = request.data['username']
        user_password = request.data['password']
        user_sex = request.data['sex']
        user_email = request.data['email']
        user_birth = request.data['birth']
        user = User.objects.create_user(
            username=user_id,
            email=user_email,
            birth=user_birth,
            sex=user_sex,
            password=user_password,
        )
        serializer = user_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 기본적인 django session login 활용
    @action(detail=False, methods=['post'], authentication_classes=[SessionAuthentication, BasicAuthentication])
    def login(self, request):
        user = self.queryset.get(username=request.data['username'])
        if check_password(request.data['password'], user.password):
            auth_user = authenticate(username=request.data['username'], password=request.data['password'])
            login(request, auth_user)
            return Response(status=status.HTTP_200_OK)

    # @action(detail=False, methods=[''])
    # def logout(self, request):



