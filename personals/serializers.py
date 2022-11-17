from rest_framework.serializers import ModelSerializer

from personals.models import Personal
from users.models import User
from users.serializers import UserSerializer
from django.core.mail import EmailMultiAlternatives


class PersonalAllSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Personal
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        validated_data["user"] = user
        email = user_data["email"]

        personal = Personal.objects.create(**validated_data)

        if personal:
            subject, from_email, to = (
                "Bem vindo ao time HealthyBody",
                "companyhealthybody@gmail.com",
                email,
            )
            text_content = "Esta é uma mensagem importante."
            html_content = f'<img src="https://http2.mlstatic.com/D_NQ_NP_946490-MLB44690797726_012021-O.webp"/>\
                <h1 style="color:#667ce0;">Olá {user.obtain_full_name()},</h1>\
                <p style="font-size: 14px">Seja bem vindo(a) a equipe <strong style="color:#667ce0;">Healthy Body</strong>!</p>\
                <p style="font-size: 14px">Agora você é um personal da melhor academia do Brasil.</p>\
                </p>\
                </p>\
                </p>\
                </p>\
                <p style="font-size: 14px">Atenciosamente,</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        return personal

    def update(self, instance, validated_data):
        try:
            request_user = validated_data.pop("user")
        except KeyError:
            request_user = False

        if request_user:
            for key, value in request_user.items():
                setattr(instance.user, key, value)
            instance.user.save()

        super().update(instance, validated_data)
        return instance
