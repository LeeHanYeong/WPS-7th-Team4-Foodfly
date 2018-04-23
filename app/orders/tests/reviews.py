from rest_framework import status
from rest_framework.test import APITestCase

from utils.test_mixins import ReverseResolveTestMixin
from ..apis import OrderReviewListCreateView
from ..models import OrderReview


class OrderReviewListTest(ReverseResolveTestMixin, APITestCase):
    MODEL = OrderReview
    VIEW = OrderReviewListCreateView
    URL = '/orders/{order__pk}/reviews/'
    VIEW_NAME = 'orders:review-list'
    URL_KWARGS = {'order__pk': 1}

    def test_blank_list(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class OrderReviewUpdateTest(APITestCase):
    MODEL = OrderReview
    VIEW = OrderReviewListCreateView
    URL = '/orders/{order__pk}/reviews/'
    VIEW_NAME = 'orders:review-list'
