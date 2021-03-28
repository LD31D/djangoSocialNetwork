from rest_framework import serializers

from .. import services
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
	is_fan = serializers.SerializerMethodField('get_is_fan', read_only=True)
	author = serializers.SerializerMethodField('get_author', read_only=True)

	class Meta:
		model = Post
		fields = ('id', 'body', 'created', 'author', 'total_likes', 'is_fan')

		extra_kwargs = {
			'author': {'required': False},
		}

	def get_author(self, obj):
		return {
				'id': obj.author.id,
				'username': obj.author.username,
				'is_active': obj.author.is_active
			}

	def get_is_fan(self, obj):
		user = self.context['request'].user
		return services.is_fan(obj, user)

	def create(self, validated_data):
		validated_data['author'] = self.context['request'].user
		return super().create(validated_data)
