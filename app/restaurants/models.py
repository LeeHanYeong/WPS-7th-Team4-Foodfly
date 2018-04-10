import datetime

from django.db import models


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=30)


class RestaurantTag(models.Model):
    name = models.CharField(max_length=30)


class RestaurantOrderType(models.Model):
    name = models.CharField(max_length=50)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    min_order_price = models.PositiveIntegerField(default=0)
    avg_delivery_time = models.TimeField(default=datetime.time(00, 00))
    restaurant_info = models.TextField(blank=True)
    origin_info = models.TextField(blank=True)

    categories = models.ManyToManyField(
        RestaurantCategory,
        verbose_name='카테고리',
        related_name='restaurants',
        blank=True,
    )
    tags = models.ManyToManyField(
        RestaurantTag,
        verbose_name='분류',
        related_name='restaurants',
        blank=True,
    )
    order_types = models.ManyToManyField(
        RestaurantOrderType,
        verbose_name='주문유형',
        related_name='restaurants',
        blank=True,
    )

    class Meta:
        verbose_name = '음식점'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name
