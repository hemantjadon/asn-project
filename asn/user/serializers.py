from rest_framework import serializers
from user.models import AuthUser
from blogs.models import Blog

class UserSerializer(serializers.HyperlinkedModelSerializer):
	blogs = serializers.HyperlinkedIdentityField(view_name='blog-detail',many=True)
	url = serializers.HyperlinkedIdentityField(view_name='user-detail')

	class Meta:
		model = AuthUser
		fields = ('url','id','username','email','blogs','is_staff')
		