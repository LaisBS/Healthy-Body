from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer
from django.core.mail import EmailMultiAlternatives

from customers.models import Customer
from users.models import User
from plans.models import Plan
from users.serializers import UserSerializer
from plans.serializers import PlanSerializer
from users.serializers import GeneralUserSerializer


class CustomerSerializer(ModelSerializer):
    user = UserSerializer()
    plan = PlanSerializer(read_only=True)
    plan_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        check_plan = validated_data.pop("plan_id")
        plan_found = get_object_or_404(Plan, id=check_plan)

        email = user_data["email"]

        user = User.objects.create_user(**user_data)

        validated_data["user"] = user

        customer = Customer.objects.create(**validated_data, plan=plan_found)

        if customer:
            subject, from_email, to = (
                "Bem vindo a HealthyBody",
                "companyhealthybody@gmail.com",
                email,
            )
            text_content = "Esta é uma mensagem importante."
            html_content = f'<img src="https://http2.mlstatic.com/D_NQ_NP_946490-MLB44690797726_012021-O.webp"/>\
                <h1 style="color:#667ce0;">Olá {user.obtain_full_name()},</h1>\
                <p style="font-size: 14px">Seja bem vindo(a) a <strong style="color:#667ce0;">Healthy Body</strong>!</p>\
                <p style="font-size: 14px">Você fez uma ótima decisão e sua saúde agradece. Agora você pode aproveitar tudo que temos de melhor.</p>\
                </p>\
                </p>\
                </p>\
                </p>\
                <p style="font-size: 14px">Atenciosamente,</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        return customer


class CustomerDetailSerializer(ModelSerializer):
    user = UserSerializer()
    plan = PlanSerializer(read_only=True)
    plan_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "user",
            "plan",
            "plan_id",
        ]
        read_only_fields = ["id"]

    def update(self, instance, validated_data):
        try:
            request_user = validated_data.pop("user")
        except KeyError:
            request_user = False

        try:
            check_plan = validated_data.pop("plan_id")
        except KeyError:
            check_plan = False

        if check_plan:
            plan_found = get_object_or_404(Plan, id=check_plan)
            setattr(instance, "plan", plan_found)
            instance.save()

        if request_user:
            for key, value in request_user.items():
                setattr(instance.user, key, value)
            instance.user.save()

        return instance


class GeneralCustomerSerializer(serializers.ModelSerializer):
    user = GeneralUserSerializer()

    class Meta:

        model = Customer
        fields = [
            "user",
        ]
