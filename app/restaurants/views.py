from django.views.generic import DetailView

from .models import Restaurant


class RestaurantDetailView(DetailView):
    model = Restaurant

    def post(self, request, pk):
        restaurant = self.get_object()
        restaurant.update_from_foodfly()
        return self.get(request, pk)
