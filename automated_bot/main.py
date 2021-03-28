import json
import requests


class User:

	def __init__(self, api_url, username, password, email=None):
		self.api_url = api_url

		self.user_data = {
							'username': username,
							'email': email,
							'password': password
						}

		# User creating
		requests.post(
				self.api_url+'api/auth/users/', 
				data=self.user_data
			)

		# Creating JWT 
		response = requests.post(
						self.api_url+'api/auth/jwt/create/', 
						data=self.user_data
					)
		self.jwt = response.json()['access']

	def create_post(self, text):
		requests.post(
				self.api_url+'api/posts/', 
				data={'body': text},
				headers={'Authorization': f'Bearer {self.jwt}'} # JWT Auth
			)


def main():
	with open('config.json', 'r') as file:
		config = json.loads(file.read())

	api_url = config['URL'] # Getting API URL

	user = User(api_url, "test1", "simple_password", "example@examle.com")
	user.create_post('Hi')


if __name__ == '__main__':
	main()
