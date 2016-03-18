from rest_framework import serializers
from blogs.models import Blog,BlogComment
from user.models import AuthUser

class BlogSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='blog-detail')
	author = serializers.HyperlinkedIdentityField(view_name='user-detail')
	comments = serializers.HyperlinkedIdentityField(many=True, view_name='blog-comment-list')
	
	class Meta:
		model = Blog
		fields = ('url','id','timestamp','author','title','content','comments')
		
class BlogCommentSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='blog-comment-detail')
	author = serializers.HyperlinkedIdentityField(view_name='user-detail')
	blog = serializers.HyperlinkedIdentityField(view_name='blog-detail')
	
	class Meta:
		model = BlogComment
		fields = ('url','id','timestamp','author','blog','comment')