from django.shortcuts import render
from blogs.serializers import BlogSerializer,BlogCommentSerializer
from blogs.models import Blog,BlogComment

from rest_framework import generics
from rest_framework import permissions

# Create your views here.

#-----------------------------------------------# 
#----------------Blog API Views-----------------#
#-----------------------------------------------# 

class BlogList(generics.ListAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	

class BlogCreate(generics.CreateAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	
	def perform_create(self,serializer):
		serializer.save(author = self.request.user)

class BlogDetail(generics.RetrieveAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

class BlogUpdate(generics.UpdateAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	
class BlogDelete(generics.DestroyAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	
	 
#--------------------X-X-X----------------------#

	

#-----------------------------------------------# 
#-------------Blog Comment API Views------------#
#-----------------------------------------------# 

class BlogCommentList(generics.ListAPIView):
	serializer_class = BlogCommentSerializer
	def get_queryset(self):
		blogID = self.kwargs['blogID']
		try:
			blog = Blog.objects.get(pk=blogID)
			return BlogComment.objects.filter(blog = blog)
		except Blog.DoesNotExist:
			blog = None
			return BlogComment.objects.none()
	
class BlogCommentCreate(generics.CreateAPIView):
	queryset = BlogComment.objects.all()
	serializer_class = BlogCommentSerializer
	
class BlogCommentDetail(generics.RetrieveAPIView):
	serializer_class = BlogCommentSerializer
	def get_queryset(self):
		blogID = self.kwargs['blogID']
		try:
			blog = Blog.objects.get(pk=blogID)
			return BlogComment.objects.filter(blog = blog)
		except Blog.DoesNotExist:
			blog = None
			return BlogComment.objects.none()
	
class BlogCommentUpdate(generics.UpdateAPIView):
	def get_queryset(self):
		blogID = self.kwargs['blogID']
		try:
			blog = Blog.objects.get(pk=blogID)
			return BlogComment.objects.filter(blog = blog)
		except Blog.DoesNotExist:
			blog = None
			return BlogComment.objects.none()
	serializer_class = BlogCommentSerializer
	
class BlogCommentDelete(generics.DestroyAPIView):
	def get_queryset(self):
		blogID = self.kwargs['blogID']
		try:
			blog = Blog.objects.get(pk=blogID)
			return BlogComment.objects.filter(blog = blog)
		except Blog.DoesNotExist:
			blog = None
			return BlogComment.objects.none()
	serializer_class = BlogCommentSerializer
 	
#--------------------X-X-X----------------------#