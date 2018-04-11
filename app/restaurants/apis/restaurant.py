from rest_framework import generics

from ..models import Restaurant
from ..serializers import RestaurantSerializer

__all__ = (
    'RestaurantListView',
)


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_fields = ('categories', 'tags', 'order_types')
