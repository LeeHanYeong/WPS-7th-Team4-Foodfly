import os

from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from rest_framework import status
from rest_framework.test import APITestCase

from restaurants.models import Restaurant, MenuCategory, Menu
from utils.decorators import after_finish
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
    reviews = []
    for i in range(num):
        order = Order.objects.create_mock(
            restaurant=restaurant,
            user=user,
            menus=[menu],
        )
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


def remove_review_images():
    for ori in OrderReviewImage.objects.all():
        ori.image.delete()


class OrderReviewListTest(ReverseResolveTestMixin, APITestCase):
    MODEL = OrderReview
    VIEW = OrderReviewListCreateView
    URL = '/orders/reviews/'
    VIEW_NAME = 'orders:review-list'

    def test_blank_list(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    @after_finish(remove_review_images)
    def test_list(self):
        num_reviews = 10
        create_image_reviews(num_reviews)
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), num_reviews)


class OrderReviewUpdateTest(ReverseResolveTestMixin, APITestCase):
    MODEL = OrderReview
    VIEW = OrderReviewRetrieveUpdateDestroyView
    URL = '/orders/reviews/{pk}/'
    VIEW_NAME = 'orders:review-detail'
    URL_KWARGS = {'pk': 1}

    @after_finish(remove_review_images)
    def test_delete_images(self):
        # 하나의 OrderReview생성
        review = create_image_reviews(1)[0]

        # 생성된 OrderReview에 연결된 OrderReviewImage List에서 pk만 가져옴
        image_pk_list = review.images.values_list('pk', flat=True)
        # 이미지가 전역변수 NUM_REVIEW_IMAGES의 개수와 같은지 확인
        self.assertEqual(len(image_pk_list), NUM_REVIEW_IMAGES)

        # 지울 이미지 pk리스트
        delete_image_pk_list = image_pk_list[::2]
        data = {
            'delete_image_pk_list': delete_image_pk_list,
        }
        # 생성된 OrderReview의 user로 인증
        self.client.force_authenticate(user=review.user)

        # 이미지를 지우는 update요청
        response = self.client.patch(
            self.URL.format(pk=review.pk), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 응답의 'images'키에 지운 이미지가 없는지 확인
        for image_data in response.data['images']:
            self.assertNotIn(image_data['pk'], delete_image_pk_list)

        # 이미지가 정상적으로 삭제되어 NUM_REVIEW_IMAGES에서 지우려고 한 개수만큼이 빠졌는지 확인
        self.assertEqual(len(response.data['images']),
                         len(image_pk_list) - len(delete_image_pk_list))
