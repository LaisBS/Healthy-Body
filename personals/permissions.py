from rest_framework import permissions
from rest_framework.views import Request, View
from personals.models import Personal


class IsSuperuserAllOrPersonalNotDelete(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Personal):
        try:
            if request.user.personal:
                return request.user.personal == obj and request.method != "DELETE"
        except AttributeError:
            return request.user.is_superuser


class IsSuperuserPersonalOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        try:
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user.personal
        except AttributeError:
            return request.user.is_superuser


class CanNotDeletePersonalUserDeleted(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return obj.user.is_active
        return True
