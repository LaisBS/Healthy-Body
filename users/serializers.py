from rest_framework.serializers import ModelSerializer
from users.models import User
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'phone', 'birthdate', 'is_active', 'password', 'email']
        read_only_fields = ('id', 'is_superuser', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}


class GeralUserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "phone",
        ]

    def get_full_name(self, obj) -> str:
        return obj.obtain_full_name()
