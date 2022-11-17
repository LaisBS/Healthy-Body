from rest_framework import serializers
from .models import Private_class
from teachers.models import Teacher
from customers.models import Customer

from django.shortcuts import get_object_or_404

from users.serializers import GeneralUserSerializer


class TeacherSerializer(serializers.ModelSerializer):

    user = GeneralUserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "user"]


class CustomerSerializerPT(serializers.ModelSerializer):

    user = GeneralUserSerializer()

    class Meta:

        model = Customer

        fields = [
            "user",
        ]


class PrivateSerializer(serializers.ModelSerializer):
    customer = CustomerSerializerPT(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Private_class
        fields = "__all__"

    def create(self, validated_data):
        check_teacher = validated_data.pop("teacher_id")
        teacher_found = get_object_or_404(Teacher, id=check_teacher)

        class_already_exists = Private_class.objects.filter(**validated_data)

        if class_already_exists:
            raise serializers.ValidationError(
                detail="You've already booked this class!"
            )

        new_private_class = Private_class.objects.create(
            **validated_data, teacher=teacher_found
        )

        return new_private_class

    def update(self, instance, validated_data):

        if len(validated_data) < 2:
            raise serializers.ValidationError(
                detail="You need to inform an date and a hour"
            )

        class_already_exists = Private_class.objects.filter(**validated_data)

        if class_already_exists:
            raise serializers.ValidationError(
                detail="You've already booked this class!"
            )

        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()

        super().update(instance, validated_data)
        return instance


class GetPrivateClasses(serializers.ModelSerializer):
    class Meta:
        model = Private_class
        fields = ["id", "date", "hour"]


class TeacherScheduleSerializer(serializers.ModelSerializer):
    private_classes = GetPrivateClasses(read_only=True, many=True)

    class Meta:
        model = Teacher
        fields = ["private_classes"]
