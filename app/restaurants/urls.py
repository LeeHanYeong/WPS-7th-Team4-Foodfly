from django.urls import path

from .apis import (
    RestaurantListView,
    RestaurantRetrieveView,
)

app_name = 'restaurants'
urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantRetrieveView.as_view(), name='restaurant-detail'),
]
