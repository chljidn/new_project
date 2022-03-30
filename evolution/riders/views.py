from riders.models import riders
from authentication.views import user_auth
from rest_framework import mixins
from rest_framework import generics

class rider_auth_view(user_auth):
    queryset = riders.objects.all()
    sub_user_model = riders
    # serializer_class = rider_serializer

# 배달 직원이 하기로 했을 경우, 해당 주문과 자신을 보낸다.
# data = 주문 객체 혹은 주문 아이디
# post, retrieve 정도만 필요
# 일단 취소나 리스트는 받지 않는다.
class delivery(mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):


    def post(self):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass