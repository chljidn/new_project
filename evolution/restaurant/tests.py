from django.test import TestCase
from rest_framework.test import APITestCase
from authentication.models import User

# class test_restaurant_request(APITestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         user = User.objects.create_user(username='user', password='user1234',
#                                         email='user@test.ev', birth='1980-01-01', sex='M')
#         owner_object = User.objects.create(username='owner', password='owner1234', email='owner@test.ev', birth='1980-01-01', sex='M', is_owner=True, is_general=False)
#         restaurant_object = restaurant.objects.create(restaurant_name='친정집 본점', phone_number='000-0000-0000', category='프랜차이즈', owner_id=owner_object)
#         product_bulk = [product(price= 15000, category='치킨', content='맛있는 후라이드 치킨', product_name='친정집 후라이드', restaurant_id=restaurant_object),
#                         product(price= 16000, category='치킨', content='맛있는 양념 치킨', product_name='친정집 양념', restaurant_id=restaurant_object),
#                         product(price= 17000, category='치킨', content='맛있는 간장 치킨', product_name='친정집 간장', restaurant_id=restaurant_object)]
#         product.objects.bulk_create(product_bulk)
#         basket.objects.create(count=2, product_id=product.objects.get(product_id=2), user_id=user)
#
#         # 유저 로그인 셋업
#         cls.login_client = APIClient()
#         cls.login_client.login(username='user', password='user1234')