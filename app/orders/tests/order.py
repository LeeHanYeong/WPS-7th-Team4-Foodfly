from rest_framework import status
from rest_framework.test import APITestCase

from utils.test_mixins import ReverseResolveTestMixin
from ..apis import OrderListCreateView
from ..models import Order

__all__ = (
    'OrderListTest',
    'OrderCreateTest',
)


class OrderListTest(ReverseResolveTestMixin, APITestCase):
    MODEL = Order
    VIEW = OrderListCreateView
    URL = '/orders/'
    VIEW_NAME = 'orders:order-list'

    def test_blank_list(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class OrderCreateTest(ReverseResolveTestMixin, APITestCase):
    MODEL = Order
    VIEW = OrderListCreateView
    URL = '/orders/'
    VIEW_NAME = 'orders:order-list'
