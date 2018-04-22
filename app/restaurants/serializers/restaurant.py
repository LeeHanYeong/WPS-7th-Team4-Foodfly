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
    name_display = serializers.CharField(source='get_name_display', read_only=True)

    class Meta:
        model = RestaurantCategory
        fields = (
            'pk',
            'name',
            'name_display',
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
    tags = RestaurantTagSerializer(many=True, read_only=True)
    categories = serializers.StringRelatedField(many=True)
    order_types = serializers.StringRelatedField(many=True)
    distance = serializers.FloatField(source='distance.m', read_only=True)

    class Meta:
        model = Restaurant
        fields = (
            'pk',
            'name',
            'address',
            'img_cover',
            'img_cover_hover',
            'min_order_price',
            'delivery_price',
            'avg_delivery_time',

            'tags',
            'categories',
            'order_types',

            'distance',
            'latitude',
            'longitude',
        )


class RestaurantRetrieveSerializer(RestaurantListSerializer):
    categories = RestaurantCategorySerializer(many=True, read_only=True)
    order_types = RestaurantOrderTypeSerializer(many=True, read_only=True)

    menu_categories = MenuCategorySerializer(many=True, read_only=True)

    class Meta(RestaurantListSerializer.Meta):
        fields = RestaurantListSerializer.Meta.fields + (
            'restaurant_info',
            'origin_info',
            'img_info',

            'categories',
            'order_types',

            'menu_categories',
        )
