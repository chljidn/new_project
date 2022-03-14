from django.shortcuts import render
from rest_framework import viewsets
from authentication.models import User
from authentication.serializers import user_serializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import sys
from django.contrib.auth import authenticate, login, logout

class sign_up(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer

    # get_object 재정의 요망
    # 회원가입
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
    # 로그인
    @action(detail=False, methods=['post'])
    def login(self, request):
        user = self.queryset.get(username=request.data['username'])
        if check_password(request.data['password'], user.password):
            auth_user = authenticate(username=request.data['username'], password=request.data['password'])
            login(request, auth_user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'message': '패스워드가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    # 로그아웃
    @action(detail=False, methods=['post'])
    def logout(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'로그아웃 되었습니다.'}, status=status.HTTP_200_OK)

    # url에 pk 문제로 데코레이터 사용. 수정 요망.
    # 회원탈퇴
    @action(detail=False, methods=['delete'])
    def withdrawal(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = self.queryset.get(username=request.user)
            if check_password(request.data['password'], user.password):
                logout(request)
                self.perform_destroy(user)
                return Response({'message':'정상적으로 탈퇴되었습니다.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': '패스워드가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

