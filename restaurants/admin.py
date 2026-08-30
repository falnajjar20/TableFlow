from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import DiningTable, Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "currency", "created_at")
    search_fields = ("name", "slug")
    ordering = ("name",)


@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "restaurant",
        "is_active",
        "qr_code_link",
        "created_at",
    )
    list_filter = ("is_active", "restaurant")
    search_fields = ("name", "restaurant__name")
    readonly_fields = (
        "qr_token",
        "qr_code_link",
        "created_at",
    )

    @admin.display(description="QR code")
    def qr_code_link(self, table):
        if not table.pk:
            return "Save the table first"

        url = reverse(
            "restaurants:table-qr",
            kwargs={"qr_token": table.qr_token},
        )

        return format_html(
            '<a href="{}" target="_blank" rel="noopener">Open QR</a>',
            url,
        )
