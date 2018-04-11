from rest_framework import serializers

from ..models import MenuCategory, Menu

__all__ = (
    'MenuCategorySerializer',
    'MenuSerializer',
)


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = (
            'pk',
            'restaurant',
            'name',
        )


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'category',
            'name',
            'price',
        )
