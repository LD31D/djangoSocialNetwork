from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
	objects = models.Manager()

	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.created.strftime('%Y-%m-%d %H:%M:%S') + " | " \
			+ " ".join(self.body.split()[:10]) + " ..."

	@property
	def total_likes(self):
		return self.likes.count()


class Like(models.Model):
	objects = models.Manager()

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
