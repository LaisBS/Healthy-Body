from rest_framework import permissions
from rest_framework.views import Request, View
from customers.models import Customer


class IsSuperuserAllOrCustomerNotDelete(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Customer):
        try:
            if request.user.customer:
                return request.user.customer == obj and request.method != "DELETE"
        except AttributeError:
            return request.user.is_superuser


class CanNotDeleteCustomerUserDeleted(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return obj.user.is_active
        return True
