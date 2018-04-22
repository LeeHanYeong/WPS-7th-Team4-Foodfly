from django.urls import path

from .apis import (
    OrderListCreateView,
)

app_name = 'orders'
urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
]
