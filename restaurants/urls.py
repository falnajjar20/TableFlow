from django.urls import path

from . import views

app_name = "restaurants"

urlpatterns = [
    path(
        "t/<uuid:qr_token>/",
        views.table_detail,
        name="table-detail",
    ),
    path(
        "t/<uuid:qr_token>/qr.png",
        views.table_qr_code,
        name="table-qr",
    ),
]
