from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from restaurant.models import restaurant
from authentication.models import User
from restaurant.serializers import owner_serializer, restaurant_serializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import backends
from restaurant.filters import restaurant_filter

# 회원 및 사장의 가입 기능 위해 공통 기능 추상화 요망(로그인, 로그아웃)
# 회원가입, 로그인/로그아웃 기능과 마이페이지 기능을 나눌까?
class owner_auth_view(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = owner_serializer

    # 전체 조회는 스태프만 가능.
    def list(self, request):
        if not request.user.IsAdminUser:
            return Response({'해당 정보를 조회할 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        owner_list = self.queryset.filter(is_owner=True)
        serializer = owner_serializer(owner_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        owner = self.queryset.create(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],
            sex=request.data['sex'],
            birth=request.data['birth'],
            is_owner=True,
            is_general=False
        )
        serializer = owner_serializer(owner)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        auth_owner = authenticate(self.request, username=request.data['username'], password=request.data['password'])
        if auth_owner is None:
            return Response({'정보가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, auth_owner)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

    def update(self):
        return Response({'해당 기능은 사용할 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        if request.user == self.get_object():
            data = super().retrieve(request, *args, **kwargs).data
            return Response(data)
        return Response({'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, reuqest):
        pass

    def withdrawal(self):
        pass

# 리스틑, 등록, 업데이트, 삭제 모두 필요하므로 일단 viewset
# 단, 업데이트와 삭제의 경우, 클라이언트의 요청이 아닌 서부 내부의 스태프만 처리할 수 있어야 하므로
# 따로 분리 가능성 있음.
class restaurant_view(viewsets.ModelViewSet):
    queryset = restaurant.objects.all()
    serializer_class = restaurant_serializer
    filter_backends = (backends.DjangoFilterBackend,)
    filterset_class = restaurant_filter

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'delete'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def create(self, request):
        if request.user.is_owner:
            self.queryset.create(
                owner_id = request.user,
                restaurant_name = request.data['restaurant_name'],
                phone_number = request.data['phone_number'],
                category=request.data['category']
            )

    def list(self):
        pass

    def delele(self):
        pass