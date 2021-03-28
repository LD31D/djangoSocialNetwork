from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


class AccountTests(APITestCase):
	user_data = {
			'username': 'TestUser', 
			'password': 'simple_password', 
			'email': 'example@exaple.com'
		}

	def create_user(self):
		url = '/api/auth/users/'

		response = self.client.post(url, self.user_data, format='json')
		self.assertEqual(
				response.data, 
				{'email': 'example@exaple.com', 'username': 'TestUser', 'id': 1}
			)

	def setUp(self):
		self.create_user()
		super().setUp()

	def test_auth_without_jwt(self):
		url = '/api/auth/users/'

		response = self.client.get(url, format='json')
		self.assertEqual(
				response.data.get('detail'), 
				'Authentication credentials were not provided.'
			)

	def test_jwt_create(self):
		url = '/api/auth/jwt/create/'

		response = self.client.post(url, self.user_data, format='json')
		jwt = response.data.get('access')
		self.assertIsNotNone(jwt)
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt)
