from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from authentication.models import User
from restaurant.models import restaurant
from django.urls import reverse

class test_restaurant_request(APITestCase):

    list_url = reverse('restaurant-list')
    detail_url = reverse('restaurant-detail', kwargs={'pk':1})
    create_data = {'restaurant_name':'홍콩반점 강남점', 'phone_number':'010-0000-0000', 'category':'chinese_food'}
    update_data = {'phone_number':'02-000-1111'}

    @classmethod
    def setUpTestData(cls):
        owner_object = User.objects.create_user(username='owner', password='owner1111', email='owner@test.ev', birth='1980-01-01', sex='M', is_owner=True, is_general=False)
        restaurant_object = restaurant.objects.create(restaurant_id=1, restaurant_name='친정집 본점', phone_number='000-0000-0000', category='Franchise', owner_id=owner_object)

        # 가맹점주 로그인 셋업
        cls.login_client = APIClient()
        cls.login_client.login(username='owner', password='owner1111')

    def test_restaurant_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_restaurant_retrieve(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_restaurant_create(self):
        response = self.login_client.post(self.list_url, self.create_data)
        self.assertEqual(response.status_code, 201)

        # 인증되지 않은 유저가 신청할 경우
        response = self.client.post(self.list_url, self.create_data)
        self.assertEqual(response.status_code, 403)

    def test_restaurant_update_error(self):
        response = self.login_client.put(self.detail_url, self.update_data)
        self.assertEqual(response.status_code, 501)

    def test_restaurant_partial_update(self):
        response = self.login_client.patch(self.detail_url, self.update_data)
        self.assertEqual(response.status_code, 202)

    def rest_restaurant_destroy(self):
        response = self.login_client.delete(self.detail_url)
        self.assertEqual(response.status_code, 200)