from rest_framework import serializers

from ..models import (
    RestaurantCategory,
    RestaurantTag,
    RestaurantOrderType,
    Restaurant
)
from ..serializers.menu import MenuCategorySerializer

__all__ = (
    'RestaurantCategorySerializer',
    'RestaurantTagSerializer',
    'RestaurantOrderTypeSerializer',
    'RestaurantListSerializer',
    'RestaurantRetrieveSerializer',
)


class RestaurantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCategory
        fields = (
            'pk',
            'name',
        )


class RestaurantTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTag
        fields = (
            'pk',
            'name',
        )


class RestaurantOrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantOrderType
        fields = (
            'pk',
            'name',
        )


class RestaurantListSerializer(serializers.ModelSerializer):
    categories = RestaurantCategorySerializer(many=True, read_only=True)
    tags = RestaurantTagSerializer(many=True, read_only=True)
    order_types = RestaurantOrderTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = (
            'pk',
            'name',
            'address',
            'min_order_price',
            'avg_delivery_time',
            'restaurant_info',
            'origin_info',

            'categories',
            'tags',
            'order_types',
        )


class RestaurantRetrieveSerializer(RestaurantListSerializer):
    menu_categories = MenuCategorySerializer(many=True, read_only=True)

    class Meta(RestaurantListSerializer.Meta):
        fields = RestaurantListSerializer.Meta.fields + (
            'menu_categories',
        )
