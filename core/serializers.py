from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
	creator = serializers.SerializerMethodField('get_creator', read_only=True)

	class Meta:
		model = Post
		fields = ('id', 'body', 'created', 'author', 'creator', 'total_likes')

		extra_kwargs = {
			'author': {'write_only': True, 'required': False},
		}

	def get_creator(self, obj):
		return {
				'id': obj.author.id,
				'username': obj.author.username,
				'is_active': obj.author.is_active
			}

	def create(self, validated_data):
		validated_data['author'] = self.context['request'].user
		return super().create(validated_data)
