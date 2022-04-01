from order.models import basket as basket_model, order, order_detail
from restaurant.models import product
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from order.serializers import basket_serializer, order_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from rest_framework import mixins
import json
from django.core.cache import cache

class basket(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = basket_model.objects.all()
    # lookup_field='username'

    def list(self, request):
        if request.user.is_staff:
            return Response(basket_serializer(self.queryset).data, status=status.HTTP_200_OK)
        return Response({'message': '일반회원은 사용할 수 없는 기능입니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, pk=None):
        if request.user.is_authenticated:
            my_basket = self.queryset.filter(user_id=pk)
            serializer = basket_serializer(my_basket, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':"로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request):
        if request.user.is_authenticated:
            product_object = product.objects.get(product_id=request.data['product_id'])
            basket_model.objects.create(
                user_id=request.user.general_user,
                product_id=product_object,
                count=request.data['count']
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # 각 장바구니에 추가된 상품마다 장바구니 테이블에서 자신만의 아이디를 가지므로 pk를 받아도 될 듯 함.
    def partial_update(self, request, pk):
        if request.user.is_authenticated:
            basket_object = self.get_object()
            basket_object.count = request.data['count']
            basket_object.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

# 해당 유저의 주문 목록, 주문 생성
# request.data : prediction_time = 현재 시각부터 배달까지 걸리는 예상 시간(분 단위)
#                product_list = 주문 목록에 들어있는 상품들의 아이디(Pk) 리스트(배열)
#                               [[pk, count],[pk,count]] 형식

class order_view(mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = order.objects.all()
    serializer_class = order_serializer
    permission_classes = [IsAuthenticated]

    # 라이더의 현재 위치 추가 요망.
    def get(self, request, *args, **kwargs):
        # my_order_filter = self.queryset.filter(user_id=request.user)
        # serializer = order_serializer(my_order_filter, many=True)
        order_data = cache.get(f"{request.user.username}_order")
        return Response(order_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        now = timezone.now()
        user_order = order.objects.create(
            user_id = request.user.general_user,
            order_time=now,
            prediction_time=now+timedelta(minutes=int(request.data['prediction_time']))
        )

        # 해당 주문 아이디에 따른 주문 상세 목록 추가
        request_data= json.loads(request.data['product_list'])
        product_id = list(map(lambda x: x[0], request_data))
        product_count = list(map(lambda x: x[1], request_data))
        bulk_order = []
        product_list = product.objects.filter(product_id__in=product_id)


        if product_list:
            for order_product, order_count in zip(product_list, product_count): # 실질적인 쿼리셋이 도는 구간
                bulk_order.append(order_detail(order_id=user_order, product_id=order_product, count=order_count))

            user_order.order_detail_set.bulk_create(bulk_order)
            serialize = order_serializer(user_order)
            if cache.has_key(f"{request.user.username}_order"):
                user_exist_order = cache.get(f"{request.user.username}_order")
                user_exist_order.append(serialize.data)
                cache.set(f"{request.user.username}_order", user_exist_order)
            else:
                cache.set(f"{request.user.username}_order", [serialize.data])
            return Response(status=status.HTTP_200_OK )

        return Response('주문할 상품이 없습니다. 주문내역을 확인해주세요.', status=status.HTTP_400_BAD_REQUEST)
