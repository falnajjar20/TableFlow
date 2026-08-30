from django.contrib import admin

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
        "qr_token",
        "created_at",
    )
    list_filter = ("is_active", "restaurant")
    search_fields = ("name", "restaurant__name")
    readonly_fields = ("qr_token", "created_at")
