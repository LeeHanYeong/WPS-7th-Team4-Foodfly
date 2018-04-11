from rest_framework import generics

from ..models import Restaurant
from ..serializers import RestaurantListSerializer, RestaurantRetrieveSerializer

__all__ = (
    'RestaurantListView',
    'RestaurantRetrieveView',
)


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    filter_fields = ('categories', 'tags', 'order_types')


class RestaurantRetrieveView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantRetrieveSerializer
