from django.urls import path

from .apis import (
    OrderListView,
)

app_name = 'orders'
urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
]
