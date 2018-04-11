from rest_framework import serializers

from ..models import MenuCategory, Menu

__all__ = (
    'MenuSerializer',
    'MenuCategorySerializer',
)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'category',
            'name',
            'info',
            'img',
            'price',
        )


class MenuCategorySerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = (
            'pk',
            'restaurant',
            'name',

            'menus',
        )
