from django.db import models


class MenuCategory(models.Model):
    restaurant = models.ForeignKey(
        'restaurants.Restaurant',
        related_name='menu_categories',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '메뉴 카테고리'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.restaurant.name} - {self.name}'


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

    class Meta:
        verbose_name = '메뉴'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.category.restaurant.name} - {self.category.name} | {self.name} ({self.price:,})'
