from django.db import models


class MenuCategory(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '메뉴 카테고리'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return self.name


class Menu(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = '메뉴'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.name} ({self.price:,})'
