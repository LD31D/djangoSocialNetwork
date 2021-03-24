from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('posts', views.PostViewSet)
# router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
