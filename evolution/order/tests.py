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

    def test_basket_create(self):
        basket_url = reverse('order:basket-list')
        self.client.login(username='user', password='user1234')
        response = self.client.post(basket_url, {"basket_list": [{"product":1, "count":1},
                                                                 {"product":3, "count":1}]}, format='json')
        self.assertEqual(response.status_code, 201)
    def test_basket_update(self):
        pass
    def test_basket_delete(self):
        pass


