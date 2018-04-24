from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from utils.permissions import IsUserOrReadOnly
from ..models import Order, OrderReview
from ..serializers import OrderReviewCreateSerializer, OrderReviewSerializer, \
    OrderReviewUpdateSerializer

__all__ = (
    'OrderReviewListCreateView',
    'OrderReviewRetrieveUpdateDestroyView',
)


class OrderReviewListCreateView(generics.ListCreateAPIView):
    queryset = OrderReview.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('order',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderReviewSerializer
        elif self.request.method == 'POST':
            return OrderReviewCreateSerializer


class OrderReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderReview.objects.all()
    permission_classes = (IsUserOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return OrderReviewUpdateSerializer
        return OrderReviewSerializer
