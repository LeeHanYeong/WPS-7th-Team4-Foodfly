import os

from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from rest_framework import status
from rest_framework.test import APITestCase

from restaurants.models import Restaurant, MenuCategory, Menu
from utils.test_mixins import ReverseResolveTestMixin
from ..apis import OrderReviewListCreateView, OrderReviewRetrieveUpdateDestroyView
from ..models import OrderReview, Order, OrderReviewImage

User = get_user_model()

NUM_REVIEW_IMAGES = 5


def create_image_reviews(num):
    user = User.objects.create_mock()
    restaurant = Restaurant.objects.create_mock()
    menu_category = MenuCategory.objects.create_mock(restaurant=restaurant)
    menu = Menu.objects.create_mock(category=menu_category)
    order = Order.objects.create_mock(
        restaurant=restaurant,
        user=user,
        menus=[menu],
    )
    reviews = []
    for i in range(num):
        review = OrderReview.objects.create_mock(
            user=user,
            order=order,
        )
        for j in range(NUM_REVIEW_IMAGES):
            file_name = f'pby{j + 1}.jpg'
            file_path = os.path.join('test', 'images', file_name)
            # storage = get_storage_class(settings.STATICFILES_STORAGE)()
            # f = storage.open(file_path)
            result = finders.find(file_path)
            OrderReviewImage.objects.create_mock(
                review=review,
                image=open(result, 'rb'),
            )
        reviews.append(review)
    return reviews


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

    def test_list(self):
        num_reviews = 10
        create_image_reviews(num_reviews)
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), num_reviews)


class OrderReviewUpdateTest(APITestCase):
    MODEL = OrderReview
    VIEW = OrderReviewRetrieveUpdateDestroyView
    URL = '/orders/{order__pk}/reviews/{pk}/'
    VIEW_NAME = 'orders:review-list'

    def test_delete_images(self):
        review = create_image_reviews(1)[0]
        image_pk_list = review.images.values_list('pk', flat=True)
        self.assertEqual(len(image_pk_list), NUM_REVIEW_IMAGES)

        delete_image_pk_list = image_pk_list[::2]
        data = {
            'delete_image_pk_list': delete_image_pk_list,
        }
        self.client.force_authenticate(user=review.user)
        response = self.client.patch(
            self.URL.format(
                order__pk=review.pk,
                pk=review.pk,
            ), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for image_data in response.data['images']:
            self.assertNotIn(image_data['pk'], delete_image_pk_list)
        self.assertEqual(len(response.data['images']), len(image_pk_list) - len(delete_image_pk_list))
