from django.db import models
import uuid


class Personal(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    check_in = models.TimeField(auto_now=False, auto_now_add=False)
    check_out = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
