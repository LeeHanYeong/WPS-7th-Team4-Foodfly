from rest_framework import serializers

from members.serializers import UserSerializer
from restaurants.serializers import RestaurantListSerializer, MenuSerializer
from .models import Order, OrderMenu


class OrderSerializer(serializers.ModelSerializer):
    restaurant = RestaurantListSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = (
            'pk',
            'restaurant',
            'user',
            'address1',
            'address2',
            'phone_number',
            'note',
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    pass


class OrderMenuSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()

    class Meta:
        model = OrderMenu
        fields = (
            'pk',
            'menu',
            'quantity',
        )
