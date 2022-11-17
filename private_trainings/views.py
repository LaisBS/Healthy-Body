from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .permissions import (
    MyCustomPermissionCustomer,
    SuperUserPermission,
    MyCustomPermissionPersonal,
    MyCustomPermissionPersonalDetail,
    MyCustomPermissionCustomerDetail,
)
from rest_framework.response import Response

from .serializers import PrivateSerializer, PersonalScheduleSerializer
from .models import Private_training


from personals.models import Personal


class PrivateViewCustomer(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionCustomer]

    def get(self, request):
        queryset = Private_training.objects.filter(
            customer_id=self.request.user.customer.id
        )
        serializer = PrivateSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = PrivateSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)


class GetAllPrivateTrainings(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserPermission]

    queryset = Private_training.objects.all()
    serializer_class = PrivateSerializer


class PrivateViewPersonal(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionPersonal]

    def get(self, request):
        queryset = Private_training.objects.filter(
            personal_id=self.request.user.personal.id
        )
        serializer = PrivateSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = PrivateSerializer


class PrivateTrainingDetailForPersonals(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionPersonalDetail]

    lookup_url_kwarg = "training_id"

    queryset = Private_training.objects.all()
    serializer_class = PrivateSerializer

    def perform_update(self, serializer):
        serializer.save(personal=self.request.user.personal)


class PrivateTrainingDetailForCustomers(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionCustomerDetail]

    lookup_url_kwarg = "training_id"

    queryset = Private_training.objects.all()
    serializer_class = PrivateSerializer

    def perform_update(self, serializer):
        serializer.save(customer=self.request.user.customer)


class PrivateSchedulePersonal(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermissionCustomer]

    lookup_url_kwarg = "personal_id"

    queryset = Personal.objects.all()
    serializer_class = PersonalScheduleSerializer
