from .models import Like


def add_like(post_obj, user_obj):
	like, is_created = Like.objects.get_or_create(post=post_obj, user=user_obj)

	return like


def remove_like(post_obj, user_obj):
	Like.objects.filter(post=post_obj, user=user_obj).delete()


def is_fan(post_obj, user_obj):
	if not user_obj.is_authenticated:
		return False

	likes = Like.objects.filter(post=post_obj, user=user_obj)
	return likes.exists()
