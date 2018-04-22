from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer

__all__ = (
    'OrderListView',
)


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
