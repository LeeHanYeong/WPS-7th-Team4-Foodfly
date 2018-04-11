from django.urls import path

from .apis import (
    RestaurantListView,
)

app_name = 'restaurants'
urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
]
