from rest_framework import serializers

from classes.models import Class
from modalities.models import Modality
from teachers.models import Teacher
from customers.models import Customer
from plans.models import Plan

from customers.serializers import GeneralCustomerSerializer
from users.serializers import GeneralUserSerializer
from django.shortcuts import get_object_or_404
from classes.exceptions import NonUpdatableKeyError, CustomValidationError


class ClassModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = [
            "id",
            "name",
        ]
        read_only_fields = [
            "name",
        ]


class ClassTeachersSerializer(serializers.ModelSerializer):

    user = GeneralUserSerializer()

    class Meta:

        model = Teacher

        fields = [
            "user",
        ]


class PostClassSerializer(serializers.ModelSerializer):
    teacher = ClassTeachersSerializer(read_only=True)
    modality = ClassModalitySerializer(read_only=True)
    modality_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Class
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True},
            "hour": {"required": True},
            "duration": {"required": True},
            "max_capacity": {"required": True},
            "vacancies": {"read_only": True},
            "customers": {"read_only": True},
        }

    def validate_max_capacity(self, value: int) -> int:
        if value < 5:
            raise serializers.ValidationError(
                "Class must have a capacity of at least 5 customers"
            )
        return value

    def create(self, validated_data):
        check_modality = validated_data.pop("modality_id")
        modality_found = get_object_or_404(Modality, id=check_modality)

        new_class = Class.objects.create(
            **validated_data,
            vacancies=validated_data["max_capacity"],
            modality=modality_found,
        )

        return new_class

    def update(self, instance, validated_data):
        forbidden_update = [
            "id",
            "modality_id",
            "teacher_id",
        ]
        errors = []

        for key, value in validated_data.items():
            if key in forbidden_update:
                errors.append({f"{key}": f"You cannot update {key} property"})
            else:
                setattr(instance, key, value)

        if len(errors) > 0:
            raise NonUpdatableKeyError(errors)

        instance.save()

        return instance


class ListClassSerializer(serializers.ModelSerializer):
    teacher = ClassTeachersSerializer(read_only=True)
    modality = ClassModalitySerializer(read_only=True)

    class Meta:
        model = Class
        fields = "__all__"


class AddCustomerSerializer(serializers.ModelSerializer):
    customers = GeneralCustomerSerializer(many=True)

    class Meta:
        model = Class

        fields = "__all__"

        read_only_fields = [
            "id",
            "name",
            "schedule",
            "hour",
            "duration",
            "max_capacity",
            "vacancies",
            "teacher",
            "modality",
        ]

    def update(self, instance, validated_data):

        user = validated_data["user"]

        customer = get_object_or_404(Customer, user=user)

        plan = get_object_or_404(Plan, id=customer.plan_id)

        check_availability = customer.classes.all()

        check_instance_in_this_class = instance.customers.filter(user=user)

        if check_instance_in_this_class:
            raise CustomValidationError("You're already part of this class.")

        if plan.name == "Bronze":
            raise CustomValidationError(
                "Your plan does not cover classes for modalities."
            )

        if plan.name == "Prata" and len(check_availability) != 0:
            raise CustomValidationError("You can only join one class per time.")

        if instance.vacancies < 1:
            raise CustomValidationError("This class is already full.")

        instance.vacancies = instance.vacancies - 1

        instance.customers.add(customer)

        instance.save()

        return instance


class RemoveCustomerSerializer(serializers.ModelSerializer):
    customers = GeneralCustomerSerializer(many=True)

    class Meta:
        model = Class

        fields = "__all__"

        read_only_fields = [
            "id",
            "name",
            "schedule",
            "hour",
            "duration",
            "max_capacity",
            "vacancies",
            "teacher",
            "modality",
        ]

    def update(self, instance, validated_data):

        user = validated_data["user"]

        customer = get_object_or_404(Customer, user=user)

        check_customer = instance.customers.filter(user=user)

        if not check_customer:
            raise CustomValidationError("You're not part of this class.")

        instance.vacancies = instance.vacancies + 1

        instance.customers.remove(customer)

        instance.save()

        return instance
