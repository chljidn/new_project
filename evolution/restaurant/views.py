from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from restaurant.models import owner
from restaurant.serializers import owner_serializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.core.cache.backends import redis

# 회원 및 사장의 가입 기능 위해 공통 기능 추상화 요망(로그인, 로그아웃)
# 회원가입, 로그인/로그아웃 기능과 마이페이지 기능을 나눌까?
class owner_auth_view(viewsets.ModelViewSet):

    queryset = owner.objects.all()

    def create(self, request):
        owner = self.queryset.create(
            ownername=request.data['username'],
            password=make_password(request.data['password']),
            phone_number=request.data['phone_number'],
            email=request.data['email']
        )
        serializer = owner_serializer(owner)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def owner_login(self, request):
        owner = self.queryset.get(ownername=request.data['ownername'])
        if check_password(request.data['password'], owner.password):
            auth_owner = authenticate(ownername=request.data['ownername'], password=request.data['password'])
            login(request, auth_owner)
            return Response(status=status.HTTP_200_OK)

    def owner_logout(self):
        pass

    def partial_update(self, reuqest):
        pass

    def owner_withdrawal(self):
        pass


# 리스틑, 등록, 업데이트, 삭제 모두 필요하므로 일단 viewset
# 단, 업데이트와 삭제의 경우, 클라이언트의 요청이 아닌 서부 내부의 스태프만 처리할 수 있어야 하므로
# 따로 분리 가능성 있음.
class restaurant_view(viewsets.ModelViewSet):
    # 카테고리 필터 요망.
    # 카테고리에 따른 가맹점 리스트
    def list(self):
        pass

    # 가맹점 등록
    # 가맹점 등록의 경우 사장의 요청 후, 내부에서 처리.
    # api의 authentications 따로 요망(스태프만 처리 가능하도록)
    def update(self, request, *args, **kwargs):

        pass

    # update와 설명 동일
    def delele(self):
        pass

