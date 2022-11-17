from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField


class Trains(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    exercises = ArrayField(models.CharField(max_length=300))
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    renovation_at = models.DateField(auto_now=False, auto_now_add=False)

    customer = models.ForeignKey(
        "customers.Customer", on_delete=models.CASCADE, related_name="trains"
    )
