from django.urls import path

from .apis import (
    OrderListCreateView,
    OrderReviewListCreateView,
    OrderReviewRetrieveUpdateDestroyView)

app_name = 'orders'
urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('reviews/', OrderReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', OrderReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
]
