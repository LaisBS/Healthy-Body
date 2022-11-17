from rest_framework import serializers
from teachers.models import Teacher
from modalities.models import Modality
from users.models import User
from users.serializers import UserSerializer
from django.core.mail import EmailMultiAlternatives


class TeacherModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = [
            "id",
            "name",
        ]


class TeachersSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    modalities = TeacherModalitySerializer(many=True, read_only=True)

    class Meta:

        model = Teacher

        fields = ["id", "user", "modalities"]

        depth = 1

    def create(self, validated_data: dict):

        request_user = validated_data.pop("user")

        user = User.objects.create_user(**request_user)

        email = request_user["email"]

        teacher = Teacher.objects.create(user=user)

        if teacher:
            subject, from_email, to = (
                "Bem vindo ao time HealthyBody",
                "companyhealthybody@gmail.com",
                email,
            )
            text_content = "Esta é uma mensagem importante."
            html_content = f'<img src="https://http2.mlstatic.com/D_NQ_NP_946490-MLB44690797726_012021-O.webp"/>\
                <h1 style="color:#667ce0;">Olá {user.obtain_full_name()},</h1>\
                <p style="font-size: 14px">Seja bem vindo(a) a equipe <strong style="color:#667ce0;">Healthy Body</strong>!</p>\
                <p style="font-size: 14px">Agora você é um professor da melhor academia do Brasil.</p>\
                </p>\
                </p>\
                </p>\
                </p>\
                <p style="font-size: 14px">Atenciosamente,</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        return teacher

    def update(self, instance: Teacher, validated_data):

        request_user = validated_data.pop("user")

        for key, value in request_user.items():
            setattr(instance.user, key, value)

        instance.user.save()

        return instance
