from django.contrib import admin
from user.models import AuthUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(AuthUser,UserAdmin)