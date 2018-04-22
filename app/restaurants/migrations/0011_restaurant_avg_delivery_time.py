# Generated by Django 2.0.4 on 2018-04-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_auto_20180418_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='avg_delivery_time',
            field=models.PositiveIntegerField(default=0, verbose_name='평균 배달시간(분)'),
        ),
    ]