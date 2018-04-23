# Generated by Django 2.0.4 on 2018-04-22 12:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성일자'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordermenu',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='orders.Order', verbose_name='주문'),
        ),
    ]