from rest_framework import generics, permissions

from utils.permissions import IsUserOrReadOnly
from ..models import OrderReview
from ..serializers import OrderReviewCreateSerializer, OrderReviewSerializer, \
    OrderReviewUpdateSerializer

__all__ = (
    'OrderReviewListCreateView',
    'OrderReviewRetrieveUpdateDestroyView',
)


class OrderReviewListCreateView(generics.ListCreateAPIView):
    queryset = OrderReview.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filterset_fields = ('order', 'user',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderReviewSerializer
        elif self.request.method == 'POST':
            return OrderReviewCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class OrderReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderReview.objects.all()
    permission_classes = (IsUserOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return OrderReviewUpdateSerializer
        return OrderReviewSerializer
