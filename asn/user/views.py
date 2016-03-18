from django.shortcuts import render
from user.serializers import UserSerializer
from user.models import AuthUser

from rest_framework import generics
from rest_framework import permissions

from user.permissions import IsAnonymous,IsSelf
# Create your views here.

class UserList(generics.ListAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
	permission_classes = ([IsAnonymous])
	queryset = AuthUser.objects.all()
	serializer_class = UserSerializer
	
class UserRetrieve(generics.RetrieveAPIView):
	permission_classes = ([permissions.IsAuthenticated])
	queryset = AuthUser.objects.all()
	serializer_class = UserSerializer
	
class UserUpdate(generics.UpdateAPIView):
	permission_classes = ([IsSelf])
	queryset = AuthUser.objects.all()
	serializer_class = UserSerializer
	
class UserDelete(generics.DestroyAPIView):
	permission_classes = ([IsSelf])
	queryset = AuthUser.objects.all()
	serializer_class = UserSerializer