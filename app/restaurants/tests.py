from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase

from .apis import RestaurantListView
from .models import Restaurant


class RestaurantListTest(APITestCase):
    MODEL = Restaurant
    VIEW = RestaurantListView
    URL = '/restaurants/'
    VIEW_NAME = 'restaurants:restaurant-list'

    TEST_RESTAURANT_NAME = 'TestRestaurantName'
    TEST_RESTAURANT_ADDRESS = 'TestRestaurantAddress'

    def create_restaurant(self, num):
        for i in range(num):
            self.MODEL.objects.create(
                name=self.TEST_RESTAURANT_NAME,
                address=self.TEST_RESTAURANT_ADDRESS,
            )

    def test_reverse(self):
        self.assertEqual(reverse(self.VIEW_NAME), self.URL)

    def test_resolve(self):
        resolver_match = resolve(self.URL)
        self.assertEqual(resolver_match.func.__name__, self.VIEW.as_view().__name__)
        self.assertEqual(resolver_match.view_name, self.VIEW_NAME)

    def test_list(self):
        test_restaurant_num = 20
        self.create_restaurant(test_restaurant_num)

        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), test_restaurant_num)
