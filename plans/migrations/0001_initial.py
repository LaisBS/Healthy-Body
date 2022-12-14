# Generated by Django 4.1.2 on 2022-11-07 21:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Plan",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                (
                    "tier",
                    models.CharField(
                        choices=[
                            ("Bronze", "Bronze"),
                            ("Prata", "Prata"),
                            ("Ouro", "Ouro"),
                            ("Não informado", "Default"),
                        ],
                        default="Não informado",
                        max_length=255,
                    ),
                ),
                ("price", models.IntegerField()),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
    ]
