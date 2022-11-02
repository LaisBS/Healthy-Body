from secrets import choice
from django.db import models
import uuid 

class Tier(models.TextChoices):
    Bronze = 'Bronze'
    SILVER = 'Silver'
    GOLD = 'Gold'
    DEFAULT = 'Não informado'

class Plan(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tier = models.CharField(max_length=255,choices=Tier.choices)
    price = models.IntegerField()
    is_active = models.BooleanField(default=False)