import json

from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase

from .apis import SignupView

User = get_user_model()


class SignupTest(APITestCase):
    MODEL = User
    VIEW = SignupView
    URL = '/members/signup/'
    VIEW_NAME = 'members:signup'

    TEST_EMAIL = 'TestEmail@test.com'
    TEST_PASSWORD = 'TestPassword'
    TEST_NAME = 'TestName'
    TEST_PHONE_NUMBER = '+82 010-1234-1234'
    TEST_PHONE_NUMBER_REP = '010-1234-1234'

    def test_reverse(self):
        self.assertEqual(reverse(self.VIEW_NAME), self.URL)

    def test_resolve(self):
        resolver_match = resolve(self.URL)
        self.assertEqual(resolver_match.func.__name__, self.VIEW.as_view().__name__)
        self.assertEqual(resolver_match.view_name, self.VIEW_NAME)

    def test_signup(self):
        data = {
            'name': self.TEST_NAME,
            'phoneNumber': self.TEST_PHONE_NUMBER,
            'email': self.TEST_EMAIL,
            'password': self.TEST_PASSWORD,
            'passwordConfirm': self.TEST_PASSWORD,
        }
        response = self.client.post(self.URL, data)

        # response.data와 생성에 사용한 값 비교
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data['user']['email'], self.TEST_EMAIL)
        self.assertEqual(response_data['user']['phoneNumber'], self.TEST_PHONE_NUMBER_REP)
        self.assertEqual(response_data['user']['name'], self.TEST_NAME)

        # response_data와 생성된 User의 속성 비교
        user = User.objects.get(pk=response_data['user']['pk'])
        self.assertEqual(response_data['user']['pk'], user.pk)
        self.assertEqual(response_data['user']['email'], user.username)
        self.assertEqual(response_data['user']['email'], user.email)
        self.assertEqual(response_data['user']['phoneNumber'], user.phone_number.as_national)
        self.assertEqual(response_data['user']['name'], user.name)
