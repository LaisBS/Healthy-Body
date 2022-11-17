from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=127, unique=True)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = [
        "phone",
        "first_name",
        "last_name",
        "birthdate",
    ]

    def obtain_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
