import datetime
import time

import re
import requests
from bs4 import BeautifulSoup
from django.core.files import File
from django.db import models, transaction
from django.db.models.signals import post_delete
from django.dispatch import receiver
from selenium import webdriver

from utils.file import download, get_buffer_ext

__all__ = (
    'RestaurantCategory',
    'RestaurantTag',
    'RestaurantOrderType',
    'Restaurant',
)


class RestaurantCategory(models.Model):
    CATEGORY_KOREAN = 'korean'
    CATEGORY_JAPANESE = 'japanese'
    CATEGORY_CAFE = 'cafe'
    CATEGORY_WESTERN = 'western'
    CATEGORY_FUSION = 'etc'
    CATEGORY_FLOUR = 'flour'
    CATEGORY_HAMBURGER = 'hamburger'
    CATEGORY_CHICKEN = 'chicken'
    CATEGORY_CHINESE = 'chinese'
    CATEGORY_PIZZA = 'pizza'
    CHOICES_CATEGORIES = (
        (CATEGORY_KOREAN, '한식'),
        (CATEGORY_JAPANESE, '일식'),
        (CATEGORY_CAFE, '카페'),
        (CATEGORY_WESTERN, '양식'),
        (CATEGORY_FUSION, '퓨전'),
        (CATEGORY_FLOUR, '분식'),
        (CATEGORY_HAMBURGER, '햄버거'),
        (CATEGORY_CHICKEN, '치킨'),
        (CATEGORY_CHINESE, '중식'),
        (CATEGORY_PIZZA, '피자'),
    )
    name = models.CharField(max_length=20, choices=CHOICES_CATEGORIES)

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


class RestaurantManager(models.Manager):
    def update_category(self, category: RestaurantCategory):
        url = f'http://www.foodfly.co.kr/restaurants?sortby=fee&category_{category.name}=on'
        client = webdriver.Chrome('/usr/local/bin/chromedriver')
        client.get(url)
        height = 0
        while True:
            client.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(1)
            body = client.find_element_by_css_selector('body')
            cur_height = body.size['height']
            if cur_height > height:
                height = cur_height
            else:
                break
        source = client.page_source
        soup = BeautifulSoup(source, 'lxml')
        a_list = soup.select('.restaurant-list > a')
        for a in a_list:
            pk = re.match(r'^.*/(?P<pk>\d+)', a.get('href', '')).group('pk').strip()
            name = a.select_one('.restaurant_info .restaurant_name').get_text(strip=True)
            bg = a.select_one('.restaurant_box span.restaurant_box_bg').get_text(strip=True)
            bg_hover = a.select_one('.restaurant_box span.restaurant_box_bg_hover').get_text(
                strip=True)
            p = re.compile(r'^url\((?P<url>.*?)\)')
            bg_url = p.match(bg).group('url')
            bg_hover_url = p.match(bg_hover).group('url')

            with transaction.atomic():
                restaurant, _ = self.get_or_create(id=pk, name=name)

                temp_file = download(bg_url)
                ext = get_buffer_ext(temp_file)
                restaurant.img_cover.save(f'{restaurant.pk}_cover.{ext}', File(temp_file))

                temp_file = download(bg_hover_url)
                ext = get_buffer_ext(temp_file)
                restaurant.img_cover_hover.save(f'{restaurant.pk}_cover_hover.{ext}', File(temp_file))
                restaurant.update_from_foodfly()

    def update_or_create_by_foodfly_id(self, foodfly_id):
        url = f'http://www.foodfly.co.kr/restaurants/show/{foodfly_id}'
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        return self.update_or_create_from_soup(foodfly_id, soup)

    def update_or_create_from_soup(self, foodfly_id, soup):
        with transaction.atomic():
            restaurant, _ = self.get_or_create(id=foodfly_id)
            restaurant.update_from_soup(soup)


class Restaurant(models.Model):
    id = models.IntegerField('푸드플라이 레스토랑 ID', primary_key=True, unique=True)
    name = models.CharField('레스토랑명', max_length=100)
    address = models.CharField('주소', max_length=200, blank=True)
    img_cover = models.ImageField('커버 이미지', upload_to='restaurant', blank=True)
    img_cover_hover = models.ImageField('커버 이미지(hover)', upload_to='restaurant', blank=True)

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

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

    def update_from_foodfly(self):
        print(f'{self.pk}] {self.name} update')
        url = f'http://www.foodfly.co.kr/restaurants/show/{self.id}'
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        return self.update_from_soup(soup)

    def update_from_soup(self, soup):
        from .menu import MenuCategory

        with transaction.atomic():
            top_box = soup.select_one('#restaurant-show > .top-box')
            left_section = top_box.select_one('.left-section')
            name = left_section.select_one('.main-info > h1').get_text(strip=True)
            thumbnail = left_section.select_one('.main-info img.restaurant-thumbnail').get('src')
            sub_info = left_section.select_one('.main-info .main-info-sub')
            sub_info_dict = {
                p.select('span')[0].get_text(strip=True):
                    p.select('span')[1].get_text(strip=True)[2:]
                for p in sub_info.select('p')
            }
            restaurant_info = soup.select_one('#restaurant-show > .restaurant-info')
            info_p_list = [p.get_text(strip=True) for p in restaurant_info.select('p') if
                           p.get_text(strip=True)]
            info = '\n'.join(info_p_list)

            restaurant_origin = soup.select('#restaurant-show > .bordered')[1]
            origin = restaurant_origin.select_one('p').get_text()

            self.name = name
            self.restaurant_info = info
            self.origin_info = origin

            self.address = sub_info_dict.get('주소', '')
            self.min_order_price = sub_info_dict.get('최소주문금액', 0)[:-2].replace(',', '').strip()
            tags = []
            for tag_name in sub_info_dict.get('분류', '').split(','):
                tag, _ = RestaurantTag.objects.get_or_create(name=tag_name.strip())
                tags.append(tag)
            self.tags.set(tags)
            order_types = []
            for order_type_name in sub_info_dict.get('주문유형', '').split(','):
                order_type, _ = RestaurantOrderType.objects.get_or_create(
                    name=order_type_name.strip())
                order_types.append(order_type)
            self.order_types.set(order_types)
            self.save()

            # 상세정보 이미지 저장
            temp_file = download(thumbnail)
            ext = get_buffer_ext(temp_file)
            self.img_info.save(f'{self.pk}.{ext}', File(temp_file))

            # 메뉴 카테고리 update 실행
            menu_container = soup.select_one('#restaurant-show > .show-menu > .left-section')
            category_list_soup = menu_container.select('.menu-category')
            for category_soup in category_list_soup:
                MenuCategory.objects.update_or_create_from_soup(self, category_soup)


@receiver(post_delete, sender=Restaurant)
def delete_img(sender, instance, created, **kwargs):
    if instance.img_cover:
        instance.img_cover.delete()
    if instance.img_cover_hover:
        instance.img_cover_hover.delete()
    if instance.img_info:
        instance.img_info.delete()
