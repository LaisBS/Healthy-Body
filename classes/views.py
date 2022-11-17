from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import Class

from .serializers import (
    ListClassSerializer,
    PostClassSerializer,
    AddCustomerSerializer,
    RemoveCustomerSerializer,
)

from utils.mixins import SerializerByMethodMixin

from classes.permissions import CustomPermission, IsAdmPermission, IsCustomerPermission

import ipdb


class ClassView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]

    queryset = Class.objects.all()
    serializer_map = {
        "GET": ListClassSerializer,
        "POST": PostClassSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.teacher)


class ClassDetailView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmPermission]

    queryset = Class.objects.all()
    serializer_map = {
        "GET": ListClassSerializer,
        "PATCH": PostClassSerializer,
    }

    lookup_url_kwarg = "class_id"


class ClassAddCustomerView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCustomerPermission]

    lookup_url_kwarg = "class_id"

    queryset = Class.objects.all()
    serializer_class = AddCustomerSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ClassRemoveCustomerView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCustomerPermission]

    lookup_url_kwarg = "class_id"

    queryset = Class.objects.all()
    serializer_class = RemoveCustomerSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ListOpenClassView(generics.ListAPIView):
    queryset = Class.objects.filter(vacancies__gt=1)
    serializer_class = ListClassSerializer
