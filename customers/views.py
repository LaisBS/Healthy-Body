from rest_framework import generics
from rest_framework.response import Response
from customers.models import Customer
from customers.serializers import CustomerDetailSerializer, CustomerSerializer
from .permissions import IsSuperuserAllOrCustomerNotDelete

from rest_framework.authentication import TokenAuthentication
from users.permissions import IsSuperuserOrReadOnly


class CreateListCustomerView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class RetrieveUpdateDeleteCustomerView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperuserAllOrCustomerNotDelete]

    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer

    lookup_url_kwarg = "customer_id"

    def perform_destroy(self, instance):
        instance.user.is_active = False
        instance.user.save()

    def delete(self, request, *args, **kwargs):
        customer = self.get_object()
        if customer.user.is_active:
            return super().delete(request, *args, **kwargs)
        return Response({"message": "User already deleted"}, status=400)
