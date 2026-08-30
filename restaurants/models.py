import uuid

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    currency = models.CharField(max_length=3, default="USD")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DiningTable(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="tables",
    )
    name = models.CharField(max_length=50)
    qr_token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)
        constraints = (
            models.UniqueConstraint(
                fields=("restaurant", "name"),
                name="unique_table_name_per_restaurant",
            ),
        )

    def __str__(self):
        return f"{self.restaurant.name} — {self.name}"
