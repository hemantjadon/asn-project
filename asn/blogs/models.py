from django.db import models
from django.conf import settings
# Create your models here.

class Blog(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='blog_author')
	timestamp = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=75,blank=False,null=True)
	content = models.TextField(blank=False,null=True)

	class Meta:
		ordering = ['-timestamp']
		
	def __str__(self):
		return "%s by %s on %s"%(self.title,self.author.get_full_name(),self.timestamp)

class BlogComment(models.Model):
	blog = models.ForeignKey(Blog,related_name='blog_comments',blank=False)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='blog_comment_author')
	timestamp = models.DateTimeField(auto_now_add=True)
	comment = models.TextField(blank=True,null=True)
	
	def __str__(self):
		return "For %s by %s on %s"%(self.blog.title,self.author.get_full_name(),self.timestamp)