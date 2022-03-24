from rest_framework.test import APITestCase, APIClient
from authentication.models import User
from django.urls import reverse
import re


class test_auth_request(APITestCase):

    session_id = None

    def setUp(self):
        user = User.objects.create_user(
            username='setup',
            password='setup1234',
            sex='M',
            birth='1991-01-10',
            email='setup@setup.com')

    def test_signup(self):
        url = reverse('authentication:signup-list')
        response = self.client.post(url, {
            'username':'test',
            'password':'test1234',
            'sex':'M',
            'birth':'1991-01-01',
            'email':'test@test.com'
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        # response = self.client.login(username="setup", password="setup1234")
        # self.assertEqual(response, True)
        login_url = reverse('authentication:signup-login')
        response = self.client.post(login_url,{
            "username":"setup",
            "password":"setup1234"
        }, format='json')
        self.assertEqual(response.status_code, 200)

        # cls.session_id = re.findall("=(.+?);", str(response.cookies['sessionid']))[0]

    def test_logout(self):
        login_url = reverse('authentication:signup-login')
        response = self.client.post(login_url,{
            "username":"setup",
            "password":"setup1234"
        }, format='json')
        session_id = re.findall("=(.+?);", str(response.cookies['sessionid']))[0]
        logout_url = reverse('authentication:signup-logout')
        response = self.client.post(logout_url)
        self.assertEqual(response.status_code, 200)


    def test_update(self):
        pass

    def test_destroy(self):
        login_url = reverse('authentication:signup-login')
        response = self.client.post(login_url, {
            "username": "setup",
            "password": "setup1234"
        }, format='json')
        self.assertEqual(response.status_code, 200)

        dt_url = reverse('authentication:signup-detail', kwargs={'username':'setup'})
        response = self.client.delete(dt_url, {'password':'setup1234'})
        self.assertEqual(response.status_code, 200)