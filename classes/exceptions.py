from rest_framework.exceptions import APIException
from rest_framework.views import status


class NonUpdatableKeyError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class CustomValidationError(APIException):
    status_code = status.HTTP_403_FORBIDDEN
