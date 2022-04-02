from riders.models import rider
from authentication.views import user_auth
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from riders.models import rider, rider_order
from order.models import order
from riders.serializers import rider_order_serializer
from django.db import transaction
from django.core.cache import cache

class rider_auth_view(user_auth):
    queryset = rider.objects.all()
    sub_user_model = rider
    # serializer_class = rider_serializer

# 배달 직원이 하기로 했을 경우, 해당 주문과 자신을 보낸다.
# data = 주문 객체 혹은 주문 아이디
# post, retrieve 정도만 필요
# 일단 취소나 전체 목록 읽기, 수정은 허용하지 않는다.
# 가맹점주의 경우, 해당 업체의 아이디에 따른 주문들을 조회할 수 있어야 함.
class delivery(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = rider_order.objects.all()
    serializer_class = rider_order_serializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        order_list = self.queryset.filter(rider_id=request.user)
        if order_list:
            serializer = self.serializer_class(order_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    # Post data : order 객체(혹은 order 번호), rider 객체
    def post(self, request, *args, **kwargs):
        if rider.objects.filter(user=request.user):
            order_object = order.objects.get(order_id=request.data['order'])
            # if not cache.haskey(f"{order_object.order_id}"):
            #     cache.set(f"{order_object.order_id}", 1)
            if not self.queryset.filter(order_id=order_object).exists():
                rider_order.objects.create(
                    order_id=order_object,
                    rider_id=request.user.rider
                )
                return Response(status=status.HTTP_201_CREATED)
            return Response({"message":"해당 요청은 받아들여지지 않았습니다. 먼저 배달을 수락한 라이더가 있습니다."},
                            status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_403_FORBIDDEN)

    # 라이더가 음식을 인도받으면 삭제.
    # 배달이 완료되고 하루 후 삭제?
    def delete(self):
        pass