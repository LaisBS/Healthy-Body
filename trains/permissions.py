from rest_framework import permissions


class IsPersonalOrCustomerReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method == "GET" and request.user.customer:
                return True
            return request.user.personal
        except AttributeError:
            return request.user.is_superuser


class IsPersonalOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.personal
        except AttributeError:
            return request.user.is_superuser
