from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase

from .apis import SignupView

User = get_user_model()


class SignupTest(APITestCase):
    MODEL = User
    VIEW = SignupView
    URL = '/signup/'
    VIEW_NAME = 'signup'

    TEST_EMAIL = 'TestEmail@test.com'
    TEST_PASSWORD = 'TestPassword'

    def test_reverse(self):
        self.assertEqual(reverse(self.VIEW_NAME), self.URL)

    def test_resolve(self):
        resolver_match = resolve(self.URL)
        self.assertEqual(resolver_match.func.__name__, self.VIEW.as_view().__name__)
        self.assertEqual(resolver_match.view_name, self.VIEW_NAME)

    def test_signup(self):
        data = {
            'email': self.TEST_EMAIL,
            'password': self.TEST_PASSWORD,
            'password_confirm': self.TEST_PASSWORD,
        }
        response = self.client.post(self.URL, data)

        # response.data와 생성에 사용한 값 비교
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user']['email'], self.TEST_EMAIL)

        # response.data와 생성된 User의 속성 비교
        user = User.objects.get(pk=response.data['user']['pk'])
        self.assertEqual(response.data['user']['pk'], user.pk)
        self.assertEqual(response.data['user']['email'], user.username)
        self.assertEqual(response.data['user']['email'], user.email)
