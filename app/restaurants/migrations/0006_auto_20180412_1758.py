# Generated by Django 2.0.4 on 2018-04-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20180411_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='푸드플라이 레스토랑 ID'),
        ),
    ]
