from django.contrib.auth import get_user_model
from rest_framework import permissions

user = get_user_model()




"""

user must be the owner of the object

"""

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsVerifiedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_verified



    
    
