from django.shortcuts import get_object_or_404, render

from .models import DiningTable


def table_detail(request, qr_token):
    table = get_object_or_404(
        DiningTable.objects.select_related("restaurant"),
        qr_token=qr_token,
        is_active=True,
    )

    return render(
        request,
        "restaurants/table_detail.html",
        {"table": table},
    )
