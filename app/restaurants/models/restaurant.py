import datetime

import requests
from bs4 import BeautifulSoup
from django.db import models, transaction
from django.db.models.signals import post_delete
from django.dispatch import receiver

__all__ = (
    'RestaurantCategory',
    'RestaurantTag',
    'RestaurantOrderType',
    'Restaurant',
)


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '음식점 카테고리'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name


class RestaurantTag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '음식점 분류'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name


class RestaurantOrderType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '음식점 주문유형'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name


class RestaurantManager(models.Model):
    def create_by_foodfly_id(self, foodfly_id):
        url = f'http://www.foodfly.co.kr/restaurants/show/{id}'
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        return self.create_from_soup(foodfly_id, soup)

    def create_from_soup(self, foodfly_id, soup):
        with transaction.atomic():
            top_box = soup.select_one('#restaurant-show > .top-box')
            left_section = top_box.select_one('.left-section')
            name = left_section.select_one('.main-info > h1').get_text(strip=True)
            thumbnail = left_section.select_one('.main-info img.restaurant-thumbnail').get('src')
            sub_info = left_section.select_one('.main-info .main-info-sub')
            sub_info_dict = {
                p.select('span')[0].get_text(strip=True): p.select('span')[1].get_text(strip=True)[
                                                          2:]
                for p in sub_info.select('p')
            }
            restaurant_info = soup.select_one('#restaurant-show > .restaurant-info')
            info_p_list = [p.get_text(strip=True) for p in restaurant_info.select('p') if
                           p.get_text(strip=True)]
            info = '\n'.join(info_p_list)

            restaurant_origin = soup.select('#restaurant-show > .bordered')[1]
            origin = restaurant_origin.select_one('p').get_text()

            restaurant = self.create(
                id=foodfly_id,
            )

            menu_container = soup.select_one('#restaurant-show > .show-menu > .left-section')
            category_list = []
            category_list_soup = menu_container.select('.menu-category')


class Restaurant(models.Model):
    id = models.IntegerField('푸드플라이 레스토랑 ID', primary_key=True, unique=True)
    name = models.CharField('레스토랑명', max_length=100)
    address = models.CharField('주소', max_length=200)
    img_cover = models.ImageField('커버 이미지', upload_to='restaurant', blank=True)

    min_order_price = models.PositiveIntegerField('최소 주문금액', default=0)
    avg_delivery_time = models.TimeField('평균 배달시간', default=datetime.time(00, 00))

    restaurant_info = models.TextField('매장소개', blank=True)
    origin_info = models.TextField('원산지 정보', blank=True)
    img_info = models.ImageField('매장소개 이미지', upload_to='restaurant-info', blank=True)

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

    objects = RestaurantManager()

    class Meta:
        verbose_name = '음식점'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Restaurant)
def delete_img(sender, instance, created, **kwargs):
    if instance.img_cover:
        instance.img_cover.delete()
    if instance.img_info:
        instance.img_info.delete()
