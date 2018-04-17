from django.urls import path

from .apis import (
    RestaurantListView,
    RestaurantRetrieveView,
)
from .views import RestaurantDetailView

app_name = 'restaurants'
urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantRetrieveView.as_view(), name='restaurant-detail'),
    path('restaurants/view/<int:pk>/', RestaurantDetailView.as_view(),
         name='view-restaurant-detail'),
]
