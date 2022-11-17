from rest_framework.serializers import ModelSerializer
from django.shortcuts import get_object_or_404
from customers.models import Customer

from trains.models import Trains
from rest_framework import serializers
from customers.serializers import CustomerSerializer
from customers.serializers import GeneralCustomerSerializer


class TrainSerializer(ModelSerializer):
    customer_id = serializers.UUIDField(write_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Trains
        fields = [
            "id",
            "customer_id",
            "customer",
            "name",
            "duration",
            "exercises",
            "created_at",
            "updated_at",
            "renovation_at",
        ]

        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        customer_id = validated_data.pop("customer_id")
        customer = get_object_or_404(Customer, id=customer_id)

        validated_data["customer"] = customer
        train = Trains.objects.create(**validated_data)
        return train


class TrainGetSerializer(ModelSerializer):
    customer = GeneralCustomerSerializer(read_only=True)

    class Meta:
        model = Trains
        fields = [
            "id",
            "name",
            "customer",
            "duration",
            "exercises",
            "created_at",
            "updated_at",
            "renovation_at",
        ]

        read_only_fields = ["id", "created_at", "updated_at"]
