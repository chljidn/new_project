from rest_framework import viewsets
from authentication.models import User
from authentication.serializers import user_serializer
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout

class user_auth(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer
    lookup_field = 'username'

    def create(self, request):
        user = User.objects.create_user(
            # **request.data
            username=request.data['username'],
            email=request.data['email'],
            birth=request.data['birth'],
            sex=request.data['sex'],
            password=request.data['password'],
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
            return Response({'message':'로그아웃 되었습니다.'}, status=status.HTTP_200_OK)


    def update(self, request, *args, **kwargs):
        pass
    def partial_update(self, request, *args, **kwargs):
        pass
    # 유저 아이디(username)를 파라미터로 받는다.
    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = self.queryset.get(username=request.user)
            if check_password(request.data['password'], user.password):
                logout(request)
                self.perform_destroy(user)
                return Response({'message':'정상적으로 탈퇴되었습니다.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': '패스워드가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)