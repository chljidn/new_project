from rest_framework import generics
from rest_framework import viewsets, status
from restaurant.models import restaurant, owner
from restaurant.serializers import owner_serializer, restaurant_serializer
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from authentication.views import user_auth, User, user_serializer

# 유저 view를 상속하여 create만 재정의
class owner_auth_view(user_auth):
    queryset = owner.objects.all()
    sub_user_model = owner
    serializer_class = owner_serializer


class restaurant_view(viewsets.ModelViewSet):
    queryset = restaurant.objects.all()
    serializer_class = restaurant_serializer
    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        parameters = {i:request.query_params[i] for i in request.query_params}
        restaurant_list = self.queryset.filter(**parameters)
        serializer = self.serializer_class(restaurant_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        if request.user.owner:
            self.queryset.create(
                owner_id=request.user.owner,
                restaurant_name=request.data['restaurant_name'],
                phone_number=request.data['phone_number'],
                category=request.data['category']
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def partial_update(self, request, *args, **kwargs):
        if request.user.owner == self.get_object().owner_id:
            super().partial_update(request, *args, **kwargs)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.owner == self.get_object().owner_id:
            super().destroy(request, *args, **kwargs)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)