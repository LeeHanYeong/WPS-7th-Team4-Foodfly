from rest_framework import generics, permissions

from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer

__all__ = (
    'OrderListCreateView',
)


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        elif self.request.method == 'POST':
            return OrderCreateSerializer
