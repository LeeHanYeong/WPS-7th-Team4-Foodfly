from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from restaurants.models import Restaurant, Menu


class Order(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, verbose_name='음식점', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='주문자', on_delete=models.CASCADE)
    address1 = models.CharField('주소1', max_length=100)
    address2 = models.CharField('주소2', max_length=100)
    phone_number = PhoneNumberField('전화번호')
    note = models.TextField('주문 요구사항', blank=True)

    def __str__(self):
        return f'주문 (PK: {self.pk})'


class OrderMenu(models.Model):
    order = models.ForeignKey(Order, verbose_name='주문', on_delete=models.CASCADE)
    menu = models.ForeignKey(
        Menu, verbose_name='메뉴', on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField('주문 수량', default=1)

    def __str__(self):
        return f'주문 메뉴 (PK: {self.pk})'