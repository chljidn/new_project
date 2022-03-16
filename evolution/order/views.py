from order.models import basket as basket_model, order, order_detail
from restaurant.models import product
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from order.serializers import basket_serializer, order_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta

# Create your views here.
# 장바구니
class basket(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = basket_model.objects.all()
    def filter_queryset(self, request):
        return self.queryset.filter(username=request.user)

    @action(detail=False, methods=['get'])
    def my_basket(self, request):
        if request.user.is_authenticated:
            basket_list = self.filter_queryset(request, self.queryset)
            serializer = basket_serializer(basket_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # 여러 객체가 들어올 경우로 수정 요망
    # ex) {basket : {product_id:1, count:1}, {상품번호 : 3, 수량:2}}
    def create(self, request):
        if request.user.is_authenticated:
            my_basket = basket_model.objects.filter(username_id=request.user) # 해당 유저의 장바구니 목록
            for detail in request.data['basket_list']:
                my_basket_detail = my_basket.filter(product_id=detail['product'])
                if my_basket_detail:
                    my_basket_detail[0].count = detail['count']
                    my_basket_detail[0].save()
                else:
                    my_basket_detail = basket_model.objects.create( # 수정 요망
                        username=request.user,
                        product_id=detail['product'],
                        count=detail['count']
                    )
                serializer = basket_serializer(my_basket, many=True)
            return Response(serializer.data)

        else:
            return Response({"message": "로그인이 필요한 기능입니다."}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        if request.user.is_authenticated:
            my_basket = self.queryset.filter(username=request.user, product_id=request.data['product'])
            my_basket.update(
                username=request.user,
                product_id=request.data['product'],
                count = request.data['count']
            )
            serializer = basket_serializer(my_basket, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request):
        pass

# 내 주문 목록(해당 유저의 모든 주문 목록 리스트)
# 주문 상세 추가에서 연산 줄일 수 있도록 수정 요망
# 결제 기능 추가 요망
class order_view(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = order.objects.all()

    # 전체 데이터가 아닌 해당 유저의 데이터만 포함하므로 수정 요망
    def list(self, request):
        order_list = self.queryset.filter(username_id=request.user)
        serializer = order_serializer(order_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 중복 체크 필요한가?
    def create(self, request):
        if request.user.is_authenticated:
            now = timezone.now()
            user_order = order.objects.create(
                username = request.user,
                # order_address =
                order_time=now,
                prediction_time=now+timedelta(minutes=int(request.data['prediction_time']))
            )

            # 해당 주문 아이디에 따른 주문 상세 목록 추가
            if request.data['my_order_list'] != []:
                for detail in request.data['my_order_list']:
                    # 추후 수정 요망
                    product_object = product.objects.get(product_id=detail['product_id'])
                    user_order.order_detail_set.create(product_id=product_object, count=detail['count'])
                return Response(status=status.HTTP_200_OK )
            else:
                return Response('주문할 상품이 없습니다. 주문내역을 확인해주세요.', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        pass