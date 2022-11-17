from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method == "POST":
                return request.user.is_authenticated and request.user.teacher
        except AttributeError:
            return False

        return request.method in permissions.SAFE_METHODS


class IsAdmPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method == "GET"
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsCustomerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method == "PATCH":
                return request.user.is_authenticated and request.user.customer
        except AttributeError:
            return False
