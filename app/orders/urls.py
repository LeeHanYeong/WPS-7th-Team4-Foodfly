from django.urls import path

from .apis import (
    OrderListCreateView,
    OrderReviewListCreateView,
)

app_name = 'orders'
urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:order__pk>/reviews/', OrderReviewListCreateView.as_view(), name='review-list'),
]
