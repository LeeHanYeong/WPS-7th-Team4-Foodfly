from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_DJANGO = 'd'
    USER_TYPE_FACEBOOK = 'f'
    CHOICES_USER_TYPE = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
    )
    type = models.CharField(max_length=1, choices=CHOICES_USER_TYPE, default=USER_TYPE_DJANGO)
    img_profile = models.ImageField(upload_to='user', blank=True)

    def __str__(self):
        return self.username
