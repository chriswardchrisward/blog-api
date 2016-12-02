from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	)

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			# 'id',
			'title',
			# 'slug',
			'content',
			'publish',
		]

post_detail_url = HyperlinkedIdentityField(
	view_name ='posts-api:detail',
	lookup_field ='slug',
	)

class PostDetailSerializer(ModelSerializer):
	url = post_detail_url
	user = SerializerMethodField()
	image = SerializerMethodField()
	html = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'id',
			'title',
			'slug',
			'content',
			'html',
			'publish',
			'image',
		]

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image

	def get_html(self, obj):
		return obj.get_markdown()

	def get_user(self, obj):
		return str(obj.user.username)

class PostListSerializer(ModelSerializer):
	url = post_detail_url
	user = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'title',
			'content',
			'publish',
		]

	def get_user(self, obj):
		return str(obj.user.username)






"""
from posts.models import Post
from posts.api.serializers import PostDetailSerializer


data = {
	"title": "Yeah buddy2",
	"content": "New content2",
	"publish": "2016-2-12",
	"slug": "yeah-buddy2"
}

obj = Post.objects.get(id=3)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
	new_item.save()
else:
	print(new_item.errors)

"""