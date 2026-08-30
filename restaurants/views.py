from io import BytesIO

import qrcode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from qrcode.constants import ERROR_CORRECT_M

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


def table_qr_code(request, qr_token):
    table = get_object_or_404(
        DiningTable,
        qr_token=qr_token,
        is_active=True,
    )

    table_url = request.build_absolute_uri(
        reverse(
            "restaurants:table-detail",
            kwargs={"qr_token": table.qr_token},
        )
    )

    qr = qrcode.QRCode(
        error_correction=ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(table_url)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="#173b32",
        back_color="white",
    )

    buffer = BytesIO()
    image.save(buffer, kind="PNG")

    response = HttpResponse(
        buffer.getvalue(),
        content_type="image/png",
    )
    response["Content-Disposition"] = f'inline; filename="table-{table.pk}-qr.png"'

    return response
