from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthUser(AbstractUser):
	
	def get_full_name(self):
		return self.first_name + " " + self.last_name
	
	def __str__(self):
		return "%s"%super(AuthUser,self).__str__()