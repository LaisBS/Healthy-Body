from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_superuser or request.method == "GET"
        )
