# Generated by Django 4.1.2 on 2022-11-07 21:49

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "schedule",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=20), size=None
                    ),
                ),
                ("hour", models.TimeField()),
                ("duration", models.CharField(max_length=20)),
                ("max_capacity", models.PositiveIntegerField()),
                ("vacancies", models.IntegerField()),
            ],
        ),
    ]