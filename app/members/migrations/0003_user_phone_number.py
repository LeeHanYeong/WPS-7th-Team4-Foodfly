# Generated by Django 2.0.4 on 2018-04-10 15:15

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20180411_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]