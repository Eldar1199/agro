from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user and bool(request.user and request.user.is_staff)
    



class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.author == request.user
    