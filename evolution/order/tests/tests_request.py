from rest_framework.test import APITestCase, APIClient
from order.models import basket
from authentication.models import User
from restaurant.models import product, restaurant, owner
from django.urls import reverse

class test_basket_request(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='user', password='user1234',
                                        email='user@test.ev', birth='1980-01-01', sex='M')
        owner_object = owner.objects.create(ownername='owner', password='owner1234', phone_number='000-0000-0000', email='owner@test.ev')
        restaurant_object = restaurant.objects.create(restaurant_name='친정집 본점', phone_number='000-0000-0000', category='프랜차이즈', owner_id=owner_object)
        product_bulk = [product(price= 15000, category='치킨', content='맛있는 후라이드 치킨', product_name='친정집 후라이드', restaurant_id=restaurant_object),
                        product(price= 16000, category='치킨', content='맛있는 양념 치킨', product_name='친정집 양념', restaurant_id=restaurant_object),
                        product(price= 17000, category='치킨', content='맛있는 간장 치킨', product_name='친정집 간장', restaurant_id=restaurant_object)]
        product.objects.bulk_create(product_bulk)
        basket.objects.create(count=2, product_id=product.objects.get(product_id=2), user_id=user)

        # 유저 로그인 셋업
        cls.login_client = APIClient()
        cls.login_client.login(username='user', password='user1234')

    def test_basket_list(self):
        basket_url = reverse('order:basket-list')
        response = self.login_client.get(basket_url)
        self.assertEqual(response.status_code, 401)

    def test_basekt_retrieve(self):
        basket_url = reverse('order:basket-detail', kwargs={'pk':1})
        response = self.login_client.get(basket_url)
        self.assertEqual(response.status_code, 200)

    def test_basket_create(self):
        basket_url = reverse('order:basket-list')
        response = self.login_client.post(basket_url, {'product_id':1, 'count':2}, format='json')
        self.assertEqual(response.status_code, 201)

    def test_basket_partial_update(self):
        basket_url = reverse('order:basket-detail', kwargs={'pk':1})
        response = self.login_client.patch(basket_url, {'count':3})
        self.assertEqual(response.status_code, 200)

    def test_basket_destroy(self):
        basket_url = reverse('order:basket-detail', kwargs={'pk':1})
        response = self.login_client.delete(basket_url)
        self.assertEqual(response.status_code, 204)

class test_order_request(APITestCase):
    def test_order_get(self):
        pass

    def test_order_post(self):
        pass