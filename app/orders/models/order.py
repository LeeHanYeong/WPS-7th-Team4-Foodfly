from random import randint

from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from restaurants.models import Restaurant, Menu

__all__ = (
    'Order',
    'OrderMenu',
)


class OrderManager(models.Manager):
    def create_mock(self, restaurant, user, menus=None):
        order = self.create(
            restaurant=restaurant,
            user=user
        )
        if menus:
            for menu in menus:
                order.menus.create_mock(order=order, menu=menu)
        return order


class Order(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, verbose_name='음식점', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='주문자', on_delete=models.CASCADE)
    address1 = models.CharField('주소1', max_length=100)
    address2 = models.CharField('주소2', max_length=100)
    phone_number = PhoneNumberField('전화번호')
    note = models.TextField('주문 요구사항', blank=True)
    created_at = models.DateTimeField('생성일자', auto_now_add=True)

    objects = OrderManager()

    def __str__(self):
        return f'주문 (PK: {self.pk})'

    @property
    def amount(self):
        return sum([order_menu.amount for order_menu in self.menus.all()])


class OrderMenuManager(models.Manager):
    def create_mock(self, order, menu):
        return self.create(
            order=order,
            menu=menu,
            quantity=randint(1, 5),
        )


class OrderMenu(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='주문',
        on_delete=models.CASCADE,
        related_name='menus',
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='메뉴',
        on_delete=models.SET_NULL,
        related_name='order_menus',
        blank=True,
        null=True,
    )
    quantity = models.IntegerField('주문 수량', default=1)

    objects = OrderMenuManager()

    def __str__(self):
        return f'주문 메뉴 (PK: {self.pk})'

    @property
    def amount(self):
        return self.menu.price * self.quantity
