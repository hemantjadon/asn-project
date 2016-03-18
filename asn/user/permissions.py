from rest_framework import permissions

class IsAnonymous(permissions.BasePermission):
    '''
        Permission only for Anonymous Users
    '''
    def has_permission(self,request,view):
        return request.user.is_anonymous()
        
    def has_object_permission(self,request,view,obj):
        return request.user.is_anonymous()

class IsSelf(permissions.BasePermission):
    '''
        Permission only for Self Objects
    '''
    def has_object_permission(self,request,view,obj):
        return obj == request.user