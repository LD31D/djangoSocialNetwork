from rest_framework.decorators import action
from rest_framework.response import Response

from .. import services


class LikedMixin:

    @action(methods=['POST', 'GET'], detail=True)
    def like(self, request, pk=None):
        post_obj = self.get_object()
        services.add_like(post_obj, request.user)

        return Response({'ok': True})

    @action(methods=['POST', 'GET'], detail=True)
    def unlike(self, request, pk=None):
        post_obj = self.get_object()
        services.remove_like(post_obj, request.user)


        return Response({'ok': True})
