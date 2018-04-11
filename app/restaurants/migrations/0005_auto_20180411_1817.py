# Generated by Django 2.0.4 on 2018-04-11 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20180411_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantcategory',
            options={'verbose_name': '음식점 카테고리', 'verbose_name_plural': '음식점 카테고리 목록'},
        ),
        migrations.AlterModelOptions(
            name='restaurantordertype',
            options={'verbose_name': '음식점 주문유형', 'verbose_name_plural': '음식점 주문유형 목록'},
        ),
        migrations.AlterModelOptions(
            name='restauranttag',
            options={'verbose_name': '음식점 분류', 'verbose_name_plural': '음식점 분류 목록'},
        ),
        migrations.AddField(
            model_name='menu',
            name='img',
            field=models.ImageField(blank=True, upload_to='menu', verbose_name='메뉴 이미지'),
        ),
        migrations.AddField(
            model_name='menu',
            name='info',
            field=models.TextField(blank=True, verbose_name='메뉴 설명'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='restaurants.MenuCategory'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=100, verbose_name='메뉴명'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.PositiveIntegerField(verbose_name='가격'),
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_categories', to='restaurants.Restaurant'),
        ),
    ]
