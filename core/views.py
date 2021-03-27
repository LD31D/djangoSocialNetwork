from rest_framework import viewsets
from rest_framework import permissions

from .models import Post
from .mixins import LikedMixin
from .serializers import PostSerializer


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
	lookup_field = 'pk'
	queryset = Post.objects.all()

	serializer_class = PostSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
