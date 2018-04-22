from django.contrib.gis.geos import Point
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

    TEST_LAT_START = 37.646988
    TEST_LAT_END = 37.523673
    TEST_LNG_START = 126.780491
    TEST_LNG_END = 127.141054

    def create_restaurant(self, num):
        for i in range(num):
            lat = self.TEST_LAT_START + (self.TEST_LAT_END - self.TEST_LAT_START) / num * i, 7
            lng = self.TEST_LNG_START + (self.TEST_LNG_END - self.TEST_LNG_START) / num * i, 7
            point = Point(lat, lng)
            self.MODEL.objects.create(
                id=i,
                name=self.TEST_RESTAURANT_NAME,
                address=self.TEST_RESTAURANT_ADDRESS,
                point=point,
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
        self.assertEqual(len(response.data['results']), test_restaurant_num)

    def test_distance_query(self):
        test_restaurant_num = 50
        test_distance = 1000
        self.create_restaurant(test_restaurant_num)
        mid_restaurant = self.MODEL.objects.all()[test_restaurant_num // 2]
        params = {
            'lat': mid_restaurant.latitude,
            'lng': mid_restaurant.longitude,
            'distance': test_distance,
        }
        response = self.client.get(self.URL, params)
        restaurant_data_list = response.data['results']
        for restaurant_data in restaurant_data_list:
            pass
