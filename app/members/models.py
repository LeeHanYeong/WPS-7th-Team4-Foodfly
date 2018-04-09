from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models
from rest_framework.authtoken.models import Token

__all__ = (
    'User',
)


class UserManager(DjangoUserManager):
    def create_email_user(self, email, password, **extra_fields):
        return self.create_user(
            username=email,
            email=email,
            password=password,
            **extra_fields
        )


class User(AbstractUser):
    USER_TYPE_DJANGO = 'd'
    USER_TYPE_FACEBOOK = 'f'
    CHOICES_USER_TYPE = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
    )
    email = models.EmailField(unique=True, blank=True)
    type = models.CharField(max_length=1, choices=CHOICES_USER_TYPE, default=USER_TYPE_DJANGO)
    img_profile = models.ImageField(upload_to='user', blank=True)

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return Token.objects.get_or_create(user=self)[0].key
