# Generated by Django 2.0.4 on 2018-04-11 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20180411_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='img_cover',
            field=models.ImageField(blank=True, upload_to='restaurant', verbose_name='커버 이미지'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='img_info',
            field=models.ImageField(blank=True, upload_to='restaurant-info', verbose_name='매장소개 이미지'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=200, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='avg_delivery_time',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='평균 배달시간'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='min_order_price',
            field=models.PositiveIntegerField(default=0, verbose_name='최소 주문금액'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, verbose_name='레스토랑명'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='origin_info',
            field=models.TextField(blank=True, verbose_name='원산지 정보'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_info',
            field=models.TextField(blank=True, verbose_name='매장소개'),
        ),
    ]