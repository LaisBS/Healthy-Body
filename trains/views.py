from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from trains.models import Trains
from trains.serializers import TrainSerializer, TrainGetSerializer
from trains.permissions import IsPersonalOrCustomerReadOnly, IsPersonalOrAdmin
from utils.mixins import SerializerByMethodMixin
from django.shortcuts import get_object_or_404
from customers.models import Customer


class CreateListTrainView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPersonalOrCustomerReadOnly]

    queryset = Trains.objects.all()

    serializer_map = {
        "GET": TrainGetSerializer,
        "POST": TrainSerializer,
    }

    def get_queryset(self):
        try:
            if self.request.user.customer:
                return self.queryset.filter(customer=self.request.user.customer)
        except AttributeError:
            return self.queryset.all()


class RetrieveUpdateDestroyTrainView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPersonalOrCustomerReadOnly]

    lookup_url_kwarg = "train_id"

    queryset = Trains.objects.all()
    serializer_class = TrainGetSerializer


class ListByCustomerView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPersonalOrAdmin]

    lookup_url_kwarg = "customer_id"

    queryset = Trains.objects.all()
    serializer_class = TrainGetSerializer

    def get_queryset(self):
        customer_id = self.kwargs["customer_id"]
        customer = get_object_or_404(Customer, id=customer_id)

        return self.queryset.filter(customer=customer)
