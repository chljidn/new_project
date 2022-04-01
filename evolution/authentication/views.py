from rest_framework import viewsets
from authentication.models import User, address_model, general_user
from authentication.serializers import user_serializer, general_user_serializer
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login, logout
from address import address_api
from django.core.cache import cache

class user_auth(viewsets.ModelViewSet):

    queryset = general_user.objects.all()
    serializer_class = general_user_serializer
    # lookup_field = 'username'
    sub_user_model = general_user

    def create(self, request, **kwargs):
        main_address = address_api(request.data['main_address'])
        user = User.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            birth=request.data['birth'],
            password=request.data['password'],
        )
        self.sub_user_model.objects.create(user=user,
                                           main_address=main_address.object,
                                           sub_address=request.data['sub_address']
                                           )

        serializer = user_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        user_object = self.queryset.get(user__username=request.data['username'])
        if check_password(request.data['password'], user_object.user.password):
            auth_user = authenticate(username=request.data['username'], password=request.data['password'])
            login(request, auth_user)
            return Response(status=status.HTTP_200_OK)
        return Response({'message': '패스워드가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'message':'로그아웃 되었습니다.'}, status=status.HTTP_200_OK)

    def list(self):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            data = super().retrieve(request, *args, **kwargs).data
            return Response(data)
        return Response({'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            kwargs['partial'] = True
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    # 유저 아이디(username)를 파라미터로 받는다.
    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_object = User.objects.get(username=request.user)
            if check_password(request.data['password'], user_object.password):
                logout(request)
                self.perform_destroy(user_object)
                return Response({'message':'정상적으로 탈퇴되었습니다.'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)




