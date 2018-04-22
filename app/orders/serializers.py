from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from members.serializers import UserSerializer
from restaurants.models import Restaurant, Menu
from restaurants.serializers import RestaurantListSerializer, MenuSerializer
from .models import Order, OrderMenu


class OrderMenuSerializer(WritableNestedModelSerializer):
    menu = MenuSerializer()

    class Meta:
        model = OrderMenu
        fields = (
            'pk',
            'menu',
            'quantity',
            'amount',
        )


class OrderMenuCreateSerializer(WritableNestedModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(),
        write_only=True,
    )

    class Meta:
        model = OrderMenu
        fields = (
            'pk',
            'menu',
            'quantity',
        )


class OrderSerializer(serializers.ModelSerializer):
    restaurant = RestaurantListSerializer()
    user = UserSerializer()
    menus = OrderMenuSerializer(many=True)
    phone_number = serializers.SerializerMethodField()

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
            'amount',
            'created_at',

            'menus',
        )

    def get_phone_number(self, obj):
        try:
            return obj.phone_number.as_national
        except:
            return obj.phone_number


class OrderCreateSerializer(WritableNestedModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),
        write_only=True,
    )
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        write_only=True,
    )
    address1 = serializers.CharField()
    address2 = serializers.CharField()
    phone_number = serializers.CharField()
    note = serializers.CharField(required=False)
    menus = OrderMenuCreateSerializer(many=True)

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

            'menus',
        )

    def to_representation(self, instance):
        return OrderSerializer(instance).data
