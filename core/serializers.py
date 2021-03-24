from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):

	creator = serializers.SerializerMethodField('get_creator', read_only=True)

	class Meta:
		model = Post
		fields = ('id', 'body', 'created', 'author', 'creator')

		extra_kwargs = {
		    'author': {'write_only': True},
		}

	def get_creator(self, obj):
		return {
				'id': obj.author.id,
				'username': obj.author.username,
				'is_active': obj.author.is_active
			}
