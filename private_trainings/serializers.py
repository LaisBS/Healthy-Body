from rest_framework import serializers
from .models import Private_training
from personals.models import Personal
from customers.models import Customer
import ipdb

from django.shortcuts import get_object_or_404

from users.serializers import GeneralUserSerializer


class PersonalSerializer(serializers.ModelSerializer):

    user = GeneralUserSerializer()

    class Meta:
        model = Personal
        fields = [
            "id",
            "user",
            "check_in",
            "check_out",
        ]
        read_only_fields = ["check_in", "check_out"]


class CustomerSerializerPT(serializers.ModelSerializer):

    user = GeneralUserSerializer()

    class Meta:

        model = Customer

        fields = [
            "user",
        ]


class PrivateSerializer(serializers.ModelSerializer):
    customer = CustomerSerializerPT(read_only=True)
    personal = PersonalSerializer(read_only=True)
    personal_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Private_training
        fields = "__all__"

    def create(self, validated_data):
        check_personal = validated_data.pop("personal_id")
        personal_found = get_object_or_404(Personal, id=check_personal)

        # hour = validated_data["hour"]

        # if hour < personal_found.check_in or hour > personal_found.check_out:
        #     raise serializers.ValidationError(
        #         detail="This workout cannot be scheduled."
        #     )

        train_already_exists = Private_training.objects.filter(**validated_data)

        if train_already_exists:
            raise serializers.ValidationError(
                detail="You've already booked this workout!"
            )

        new_private_training = Private_training.objects.create(
            **validated_data, personal=personal_found
        )

        return new_private_training

    def update(self, instance, validated_data):
        if len(validated_data) < 3:
            raise serializers.ValidationError(
                detail="You need to inform an date, hour and a personal_id"
            )

        train_already_exists = Private_training.objects.filter(**validated_data)

        if train_already_exists:
            raise serializers.ValidationError(
                detail="You've already booked this workout!"
            )
        # personal_found = get_object_or_404(Personal, id=instance.personal.id)

        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()

        super().update(instance, validated_data)
        return instance


class GetPrivateTrainings(serializers.ModelSerializer):
    class Meta:
        model = Private_training
        fields = [
            "date",
            "hour",
        ]


class PersonalScheduleSerializer(serializers.ModelSerializer):
    private_trainings = GetPrivateTrainings(read_only=True, many=True)

    class Meta:
        model = Personal
        fields = [
            "check_in",
            "check_out",
            "private_trainings",
        ]
