from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	)

from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment

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
	user = UserDetailSerializer(read_only=True)
	image = SerializerMethodField()
	html = SerializerMethodField()
	comments = SerializerMethodField()
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
			'comments',
		]

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image

	def get_html(self, obj):
		return obj.get_markdown()

	def get_comments(self, obj):
		content_type = obj.get_content_type
		object_id = obj.id
		c_qs = Comment.objects.filter_by_instance(obj)
		comments = CommentSerializer(c_qs, many=True).data
		return comments


class PostListSerializer(ModelSerializer):
	url = post_detail_url
	user = UserDetailSerializer(read_only=True)
	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'title',
			'content',
			'publish',
		]







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