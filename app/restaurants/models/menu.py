from random import randint

from django.core.files import File
from django.db import models, transaction

from utils.file import download, get_buffer_ext


class MenuCategoryManager(models.Manager):
    def update_or_create_from_soup(self, restaurant, soup):
        """
        :param soup:
            #restaurant-show
                > .show-menu
                    > .left-section
                        .menu-category (list)
        :return:
        """
        category_name = soup.select_one('.row-category').get_text(strip=True)
        with transaction.atomic():
            category, _ = self.update_or_create(
                restaurant=restaurant,
                name=category_name,
            )
            menu_soup_list = soup.select('.row-menu')
            for menu_soup in menu_soup_list:
                Menu.objects.update_or_create_from_soup(category, menu_soup)

    def create_mock(self, restaurant):
        return self.create(
            restaurant=restaurant,
            name='Mock menu category'
        )


class MenuCategory(models.Model):
    restaurant = models.ForeignKey(
        'restaurants.Restaurant',
        related_name='menu_categories',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)

    objects = MenuCategoryManager()

    class Meta:
        verbose_name = '메뉴 카테고리'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.restaurant.name} - {self.name}'


class MenuManager(models.Manager):
    def update_or_create_from_soup(self, category, soup):
        name = soup.select_one('.col-menu > strong').get_text(strip=True)
        info = soup.select_one('.col-menu > span').get_text(strip=True)
        photo_soup = soup.select_one('.col-photo > img')
        photo = photo_soup.get('src') if photo_soup else ''
        price = soup.select_one('.col-price > .price').get_text(strip=True).replace(',', '')

        menu, _ = self.update_or_create(
            category=category,
            name=name,
            defaults={
                'info': info,
                'price': price,
            }
        )
        if photo:
            temp_file = download(photo)
            ext = get_buffer_ext(temp_file)
            menu.img.save(f'{menu.pk}.{ext}', File(temp_file))

    def create_mock(self, category):
        return self.create(
            category=category,
            name='Mock menu name',
            price=randint(1, 10) * 1000
        )


class Menu(models.Model):
    category = models.ForeignKey(
        MenuCategory,
        related_name='menus',
        on_delete=models.CASCADE,
    )
    name = models.CharField('메뉴명', max_length=100)
    info = models.TextField('메뉴 설명', blank=True)
    img = models.ImageField('메뉴 이미지', upload_to='menu', blank=True)
    price = models.PositiveIntegerField('가격')

    objects = MenuManager()

    class Meta:
        verbose_name = '메뉴'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.category.restaurant.name} - {self.category.name} | ' \
               f'{self.name} ({self.price:,})'
