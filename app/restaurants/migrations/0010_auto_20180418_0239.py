# Generated by Django 2.0.4 on 2018-04-17 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_restaurant_delivery_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ('-pk',), 'verbose_name': '음식점', 'verbose_name_plural': '음식점 목록'},
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='avg_delivery_time',
        ),
    ]
