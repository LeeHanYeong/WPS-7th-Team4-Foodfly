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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    query_fields = ('order__pk',)

    def get_order(self):
        order_pk = self.kwargs['order__pk']
        order = get_object_or_404(Order, pk=order_pk)
        return order

    def get_queryset(self):
        filter = {field: self.kwargs[field] for field in self.query_fields if self.kwargs[field]}
        return OrderReview.objects.filter(**filter)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderReviewSerializer
        elif self.request.method == 'POST':
            return OrderReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save(order=self.get_order())


class OrderReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserOrReadOnly,)
    query_fields = ('order__pk',)

    def get_queryset(self):
        filter = {field: self.kwargs[field] for field in self.query_fields if self.kwargs[field]}
        return OrderReview.objects.filter(**filter)

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return OrderReviewUpdateSerializer
        return OrderReviewSerializer
