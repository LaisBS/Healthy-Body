from rest_framework import permissions
from rest_framework.views import Request
from .models import Teacher


class IsAdminOrOwnerOrReadyOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser

    def has_object_permission(self, request: Request, view, obj: Teacher):

        return request.user.is_superuser or request.user == obj.user
