from django.urls import path

from . import views

app_name = "restaurants"

urlpatterns = [
    path(
        "t/<uuid:qr_token>/",
        views.table_detail,
        name="table-detail",
    ),
]
