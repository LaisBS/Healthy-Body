from rest_framework import permissions
from rest_framework.views import Request, View
from teachers.models import Teacher
from customers.models import Customer


class MyCustomPermissionCustomer(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        try:
            if request.method == "POST" or request.method == "GET":
                return request.user.is_authenticated and request.user.customer
        except AttributeError:
            return False


class MyCustomPermissionCustomerDetail(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, customer: Customer):
        try:
            if request.method == "PATCH" or request.method == "GET":
                return (
                    request.user.is_authenticated
                    and request.user.customer
                    and request.user == customer.customer.user
                )
        except AttributeError:
            return False


class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.user.is_authenticated and request.user.is_superuser:
            return True


class MyCustomPermissionTeacher(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        try:
            if request.method == "GET":
                return request.user.is_authenticated and request.user.teacher
        except AttributeError:
            return False


class MyCustomPermissionTeacherDetail(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, teacher: Teacher
    ) -> bool:
        try:
            if (
                request.method == "DELETE"
                or request.method == "PATCH"
                or request.method == "GET"
            ):
                return (
                    request.user.is_authenticated
                    and request.user.teacher
                    and request.user == teacher.teacher.user
                )
        except AttributeError:
            return False
