from django import forms
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django_filters import rest_framework as filters

from ..models import Restaurant


class RestaurantFilter(filters.FilterSet):
    name = filters.LookupChoiceFilter(
        field_class=forms.CharField,
        lookup_choices=[
            ('icontains', 'Contains'),
        ]
    )
    tags__name = filters.LookupChoiceFilter(
        field_class=forms.CharField,
        lookup_choices=[
            ('icontains', 'Contains'),
        ]
    )
    # name = filters.CharFilter(lookup_expr='icontains')
    # tags__name = filters.CharFilter(name='tags__name', lookup_expr='icontains')

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'tags__name',
            'categories',
        ]

    @property
    def qs(self):
        parent = super().qs
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')
        distance = self.request.query_params.get('distance')
        if lat and lng and distance:
            point = Point(float(lat), float(lng))
            return parent \
                .filter(point__distance_lte=(point, distance)) \
                .annotate(distance=Distance('point', point))
        return super().qs
