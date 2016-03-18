from django.db import models
from django.conf import settings

import uuid
# Create your models here.

class Blog(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='blogs')
	timestamp = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=75,blank=False,null=True)
	content = models.TextField(blank=False,null=True)

	class Meta:
		ordering = ['-timestamp']
		
	def __str__(self):
		return "%s by %s on %s"%(self.title,self.author.get_full_name(),self.timestamp)

class BlogComment(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	blog = models.ForeignKey(Blog,related_name='comments',blank=False)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='blog_comment')
	timestamp = models.DateTimeField(auto_now_add=True)
	comment = models.TextField(blank=True,null=True)
	
	def __str__(self):
		return "For %s by %s on %s"%(self.blog.title,self.author.get_full_name(),self.timestamp)