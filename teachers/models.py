from django.db import models
from users.models import User
import uuid


class Teacher(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
