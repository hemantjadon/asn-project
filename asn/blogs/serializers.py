from rest_framework import serializers
from rest_framework.reverse import reverse
from blogs.models import Blog,BlogComment
from user.models import AuthUser

class CustomHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
	
	def get_url(self, obj, view_name, request, format):
		url_kwargs = {
			'blogID': obj.blog.id,
			'pk': obj.id
		}
		return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

	def get_object(self, view_name, view_args, view_kwargs):
		lookup_kwargs = {
			'blog__id': view_kwargs['blogID'],
			'pk': view_kwargs['id']
		}
		return self.get_queryset().get(**lookup_kwargs)

class CustomAuthorHyperlinkIdentityField(serializers.HyperlinkedIdentityField):
		def get_url(self, obj, view_name, request, format):
			url_kwargs = {
				'pk': obj.author.pk
			}
			return reverse(view_name, kwargs=url_kwargs, request=request, format=format)
		def get_object(self, view_name, view_args, view_kwargs):
			lookup_kwargs = {
				'pk': view_args['pk']
			}
			return self.get_queryset().get(**lookup_kwargs)
		
class BlogSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='blog-detail',lookup_field='pk')
	author = CustomAuthorHyperlinkIdentityField(view_name='user-detail')
	comments = CustomHyperlinkedIdentityField(many=True, view_name='blog-comment-detail',lookup_field='pk')
	
	class Meta:
		model = Blog
		fields = ('url','id','timestamp','author','title','content','comments')
		
class BlogCommentSerializer(serializers.HyperlinkedModelSerializer):
	url = CustomHyperlinkedIdentityField(view_name='blog-comment-detail',lookup_field='pk')
	author = CustomAuthorHyperlinkIdentityField(view_name='user-detail')
	blog = serializers.HyperlinkedIdentityField(view_name='blog-detail',lookup_field='pk')
	
	class Meta:
		model = BlogComment
		fields = ('url','id','timestamp','author','blog','comment')