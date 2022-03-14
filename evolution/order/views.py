from order.models import basket as basket_model, order
from restaurant.models import product
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from order.serializers import basket_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.
# 장바구니
class basket(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = basket_model.objects.all()
    def filter_queryset(self, request, queryset):
        return queryset.filter(username=request.user)

    @action(detail=False, methods=['get'])
    def my_basket(self, request):
        if request.user.is_authenticated:
            basket_list = self.filter_queryset(request, self.queryset)
            serializer = basket_serializer(basket_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # 여러 객체가 들어올 경우로 수정 요망
    # ex) [{상품번호:1, 이름: 네내치킨 후라이드, 수량:1}, {상품번호 : 5, 이름: 네네치킨 간장, 수량:2}]
    def create(self, request):
        if request.user.is_authenticated:
            my_basket = basket_model.objects.filter(username=request.user, product_id = request.data['product'])
            product_id = product.objects.get(product_id=request.data['product'])
            if my_basket:
                my_basket[0].count = request.data['count']
                my_basket[0].save()
            else:
                my_basket = basket_model.objects.create(
                    username=request.user,
                    product_id=product_id,
                    count=request.data['count']
                )
            serializer = basket_serializer(my_basket)
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
# 해당 주문의 상세 내역(해당 유저의 해당 주문의 상세 내역) < = 이 부분은 주문 상세로 가야 할 듯?
# 결제 기능 추가해야 하므로 뒤로 미룸

class order_view(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def create(self, request):
        pass

    def delete(self, request):
        pass