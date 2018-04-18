from django_filters import rest_framework as filters

from ..models import Restaurant


class RestaurantFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    tags__name = filters.CharFilter(name='tags__name', lookup_expr='icontains')

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'tags__name',
            'categories',
        ]
