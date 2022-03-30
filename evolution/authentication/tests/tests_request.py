from rest_framework.test import APITestCase, APIClient
from authentication.models import User, general_user
from django.urls import reverse
import re


class test_auth_request(APITestCase):

    def setUp(self):
        user = User.objects.create_user(id= 1, username='setup',password='setup1234',birth='1991-01-10',email='setup@setup.com')
        user_object = general_user.objects.create(user=user)

    def test_signup(self):
        url = reverse('authentication:user-list')
        response = self.client.post(url, {
            'username':'test',
            'password':'test1234',
            'birth':'1991-01-01',
            'email':'test@test.com'
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        login_url = reverse('authentication:user-login')
        response = self.client.post(login_url,{
            "username":"setup",
            "password":"setup1234"
        }, format='json')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        login_url = reverse('authentication:user-login')
        response = self.client.post(login_url,{
            "username":"setup",
            "password":"setup1234"
        }, format='json')
        session_id = re.findall("=(.+?);", str(response.cookies['sessionid']))[0]

        logout_url = reverse('authentication:user-logout')
        response = self.client.post(logout_url)
        self.assertEqual(response.status_code, 200)


    def test_update(self):
        pass

    def test_destroy(self):
        login_url = reverse('authentication:user-login')
        response = self.client.post(login_url, {
            "username": "setup",
            "password": "setup1234"
        }, format='json')
        self.assertEqual(response.status_code, 200)

        dt_url = reverse('authentication:user-detail', kwargs={"pk":1})
        response = self.client.delete(dt_url, {'password':'setup1234'})
        self.assertEqual(response.status_code, 200)