from rest_framework import generics

from utils.pagination import Pagination20
from ..filters import RestaurantFilter
from ..models import Restaurant, RestaurantCategory
from ..serializers import RestaurantListSerializer, RestaurantRetrieveSerializer, \
    RestaurantCategorySerializer

__all__ = (
    'RestaurantCategoryListView',
    'RestaurantListView',
    'RestaurantRetrieveView',
)


class RestaurantCategoryListView(generics.ListAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    pagination_class = Pagination20
    filterset_class = RestaurantFilter
    search_fields = ('name', 'tags__name')
    ordering_fields = ('min_order_price', 'delivery_price', 'avg_delivery_time')


class RestaurantRetrieveView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantRetrieveSerializer
