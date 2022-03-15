from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action


# 회원 및 사장의 가입 기능 위해 공통 기능 추상화 요망(로그인, 로그아웃)
# 회원가입, 로그인/로그아웃 기능과 마이페이지 기능을 나눌까?
class owner_auth_view(generics.UpdateAPIView):
    def owner_sign_up(self, request):
        pass

    def owner_login(self):
        pass

    def owner_logout(self):
        pass

# 가맹점 사장의 (내 정보) 기능
class owner_my_page_view(generics.ListAPIView, generics.UpdateAPIView):
    def owner_detail(self, pk=None):
        pass

    def owner_detail_update(self, reuqest):
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

