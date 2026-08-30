import uuid

from django.test import TestCase
from django.urls import reverse

from .models import DiningTable, Restaurant


class TableDetailTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            slug="test-restaurant",
            currency="USD",
        )
        cls.table = DiningTable.objects.create(
            restaurant=cls.restaurant,
            name="Table 1",
        )

    def get_table_url(self, qr_token=None):
        token = qr_token or self.table.qr_token

        return reverse(
            "restaurants:table-detail",
            kwargs={"qr_token": token},
        )

    def get_qr_url(self):
        return reverse(
            "restaurants:table-qr",
            kwargs={"qr_token": self.table.qr_token},
        )

    def test_active_table_page_loads(self):
        response = self.client.get(self.get_table_url())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "restaurants/table_detail.html",
        )
        self.assertContains(response, "Test Restaurant")
        self.assertContains(response, "Table 1")

    def test_unknown_qr_token_returns_404(self):
        response = self.client.get(
            self.get_table_url(uuid.uuid4()),
        )

        self.assertEqual(response.status_code, 404)

    def test_inactive_table_returns_404(self):
        self.table.is_active = False
        self.table.save(update_fields=["is_active"])

        response = self.client.get(self.get_table_url())

        self.assertEqual(response.status_code, 404)

    def test_qr_code_returns_png_image(self):
        response = self.client.get(self.get_qr_url())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "image/png")
        self.assertTrue(response.content.startswith(b"\x89PNG\r\n\x1a\n"))

    def test_inactive_table_qr_returns_404(self):
        self.table.is_active = False
        self.table.save(update_fields=["is_active"])

        response = self.client.get(self.get_qr_url())

        self.assertEqual(response.status_code, 404)
