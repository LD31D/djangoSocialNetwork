import json
import random
import string 

import requests


class User:

	def __init__(self, API_URL, username, password, email=None):
		self.API_URL = API_URL

		self.user_data = {
							'username': username,
							'email': email,
							'password': password
						}

		# User creating
		requests.post(
				self.API_URL + 'api/auth/users/', 
				data=self.user_data
			)

		# Creating JWT 
		response = requests.post(
						self.API_URL + 'api/auth/jwt/create/', 
						data=self.user_data
					)
		self.jwt = response.json()['access']

	def create_post(self, text: str):
		requests.post(
				self.API_URL + 'api/posts/', 
				data={'body': text},
				headers={'Authorization': f'Bearer {self.jwt}'} # JWT Auth
			)

	def get_all_posts(self) -> list:
		response = requests.get(
						self.API_URL + 'api/posts/',
						headers={'Authorization': f'Bearer {self.jwt}'}
					)

		return response.json()

	def get_unliked_posts(self) -> list:
		all_posts = self.get_all_posts() # Getting all posts 
		# Filtering posts that have been already liked
		unliked_posts = list(filter(lambda post: post['is_fan'] == False, all_posts))

		return unliked_posts

	def like_post(self, post_id: int):
		requests.post(
			self.API_URL + f'api/posts/{post_id}/like/',
			headers={'Authorization': f'Bearer {self.jwt}'}
		)


def generate_username() -> str:
	letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
	username = 'User_' + ''.join(random.choice(letters) for _ in range(5))

	return username 


def main():
	with open('config.json', 'r') as file:
		config = json.loads(file.read()) # Reading data from config file

	for _ in range(config['NUMBER_OF_USERS']): # Iteration for user creating
		username = generate_username() # Getting username for new user

		print(f"|---------- Username: {username} ----------|")

		user = User(config['URL'], username, "simple_password") # Creating new user

		# Iteration for posts creating
		for _ in range(random.randrange(config['MAX_POSTS_PER_USER']+1)):
			joke = requests.get(
						'https://icanhazdadjoke.com', 
						headers={"Accept": "text/plain"}
					).text # Getting random joke from other API

			user.create_post(joke)
			print(joke + '\n')

		unliked_posts = user.get_unliked_posts()
		for _ in range(config['MAX_LIKES_PER_USER']):
			
			# If list is free, we are stopping the loop
			if not unliked_posts:
				break

			unliked_post = random.choice(unliked_posts) # Get random post from unliked posts

			user.like_post(unliked_post['id']) # Like this post
			print(f"Liked: {unliked_post['id']}")

			unliked_posts.remove(unliked_post) # Delete this post from unliked posts list


if __name__ == '__main__':
	main()
