from rest_framework import serializers

from ..models import (
    RestaurantCategory,
    RestaurantTag,
    RestaurantOrderType,
    Restaurant)


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


class RestaurantSerializer(serializers.ModelSerializer):
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
