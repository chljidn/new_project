from rest_framework import generics
from rest_framework import viewsets, status
from restaurant.models import restaurant
from restaurant.serializers import owner_serializer, restaurant_serializer
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import backends
from restaurant.filters import restaurant_filter
from authentication.views import user_auth, User, user_serializer
from restaurant.models import owner

# 유저 view를 상속하여 create만 재정의
class owner_auth_view(user_auth):
    sub_user_model = owner

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
        if request.user.is_owner or request.user.IsAdminUser:
            self.queryset.create(
                owner_id=request.user,
                restaurant_name=request.data['restaurant_name'],
                phone_number=request.data['phone_number'],
                category=request.data['category']
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object().owner_id or request.user.IsAdminUser:
            super().partial_update(request, *args, **kwargs)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().owner_id or request.user.IsAdminUser:
            super().destroy(request, *args, **kwargs)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)