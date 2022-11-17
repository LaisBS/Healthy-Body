from django.db import models
import uuid


class Private_training(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date = models.DateField()
    hour = models.TimeField()
    update_at = models.DateTimeField(auto_now=True)

    customer = models.ForeignKey(
        "customers.Customer", on_delete=models.CASCADE, related_name="private_trainings"
    )

    personal = models.ForeignKey(
        "personals.Personal", on_delete=models.CASCADE, related_name="private_trainings"
    )
