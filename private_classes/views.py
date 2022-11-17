from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .permissions import (
    MyCustomPermissionCustomer,
    SuperUserPermission,
    MyCustomPermissionTeacher,
    MyCustomPermissionTeacherDetail,
    MyCustomPermissionCustomerDetail,
)
from rest_framework.response import Response

from .serializers import PrivateSerializer, TeacherScheduleSerializer
from .models import Private_class
from teachers.models import Teacher


class PrivateViewCustomer(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionCustomer]

    def get(self, request):
        queryset = Private_class.objects.filter(
            customer_id=self.request.user.customer.id
        )
        serializer = PrivateSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = PrivateSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)


class GetAllPrivateClasses(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserPermission]

    queryset = Private_class.objects.all()
    serializer_class = PrivateSerializer


class PrivateViewPersonal(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionTeacher]

    def get(self, request):

        queryset = Private_class.objects.filter(teacher_id=self.request.user.teacher.id)
        print(self.request.user)
        serializer = PrivateSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = PrivateSerializer


class PrivateClassesDetailForTeachers(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionTeacherDetail]

    lookup_url_kwarg = "class_id"

    queryset = Private_class.objects.all()
    serializer_class = PrivateSerializer

    def perform_update(self, serializer):
        serializer.save(teacher=self.request.user.teacher)


class PrivateClassesDetailForCustomers(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionCustomerDetail]

    lookup_url_kwarg = "class_id"

    queryset = Private_class.objects.all()
    serializer_class = PrivateSerializer

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user.customer)


class PrivateScheduleTeacher(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionCustomer]

    lookup_url_kwarg = "teacher_id"

    queryset = Teacher.objects.all()
    serializer_class = TeacherScheduleSerializer
