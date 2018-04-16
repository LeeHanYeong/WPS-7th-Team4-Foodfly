from django.db import models, transaction


class MenuCategoryManager(models.Manager):
    def create_from_soup(self, restaurant, soup):
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
            category = self.create(
                restaurant=restaurant,
                name=category_name,
            )
            menu_soup_list = soup.select('.row-menu')
            for menu_soup in menu_soup_list:
                Menu.objects.create_from_soup(category, menu_soup)


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
    def create_from_soup(self, category, soup):
        name = soup.select_one('.col-menu > strong').get_text(strip=True)
        info = soup.select_one('.col-menu > span').get_text(strip=True)
        photo_soup = soup.select_one('.col-photo > img')
        photo = photo_soup.get('src') if photo_soup else ''
        price = soup.select_one('.col-price > .price').get_text(strip=True).replace(',', '')

        self.create(
            category=category,
            name=name,
            info=info,
            price=price,
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
