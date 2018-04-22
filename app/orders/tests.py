from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Order
from .apis import OrderListView


class OrderListTest(APITestCase):
    MODEL = Order
    VIEW = OrderListView
    URL = '/orders/'
    VIEW_NAME = 'orders:order-list'

    def test_reverse(self):
        self.assertEqual(reverse(self.VIEW_NAME), self.URL)

    def test_resolve(self):
        resolver_match = resolve(self.URL)
        self.assertEqual(resolver_match.func.__name__, self.VIEW.as_view().__name__)
        self.assertEqual(resolver_match.view_name, self.VIEW_NAME)

    def test_blank_list(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
