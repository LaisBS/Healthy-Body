from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField


class Class(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    schedule = ArrayField(models.CharField(max_length=20))
    hour = models.TimeField()
    duration = models.CharField(max_length=20)
    max_capacity = models.PositiveIntegerField()
    vacancies = models.IntegerField()

    teacher = models.ForeignKey(
        "teachers.Teacher", on_delete=models.CASCADE, related_name="classes"
    )

    modality = models.ForeignKey(
        "modalities.Modality", on_delete=models.CASCADE, related_name="classes"
    )

    customers = models.ManyToManyField(
        "customers.Customer",
        related_name="classes",
    )
