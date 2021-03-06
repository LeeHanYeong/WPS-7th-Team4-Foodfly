# Generated by Django 2.0.4 on 2018-04-11 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_menu_menucategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.MenuCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menucategory',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant'),
            preserve_default=False,
        ),
    ]
