from django.db import models
import uuid


class Modality(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30, unique=True)

    teacher = models.ForeignKey(
        "teachers.Teacher", on_delete=models.CASCADE, related_name="modalities"
    )
