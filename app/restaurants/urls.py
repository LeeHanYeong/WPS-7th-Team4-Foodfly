from django.urls import path

from .apis import (
    RestaurantCategoryListView,
    RestaurantListView,
    RestaurantRetrieveView,
)
from .views import RestaurantDetailView

app_name = 'restaurants'
urlpatterns = [
    path('restaurants/categories/', RestaurantCategoryListView.as_view(), name='category-list'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantRetrieveView.as_view(), name='restaurant-detail'),
    path('restaurants/view/<int:pk>/', RestaurantDetailView.as_view(),
         name='view-restaurant-detail'),
]
