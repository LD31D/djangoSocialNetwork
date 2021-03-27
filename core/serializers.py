from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
	author = serializers.SerializerMethodField('get_author', read_only=True)

	class Meta:
		model = Post
		fields = ('id', 'body', 'created', 'author', 'total_likes')

		extra_kwargs = {
			'author': {'required': False},
		}

	def get_author(self, obj):
		return {
				'id': obj.author.id,
				'username': obj.author.username,
				'is_active': obj.author.is_active
			}

	def create(self, validated_data):
		validated_data['author'] = self.context['request'].user
		return super().create(validated_data)
