# Generated by Django 2.0.4 on 2018-04-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20180416_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='delivery_price',
            field=models.PositiveIntegerField(default=0, verbose_name='배달팁'),
        ),
    ]
