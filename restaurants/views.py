from django.shortcuts import render
from django.views.generic import ListView

from .models import RestaurantLocation

# Create your views here.
class RestaurantsListView(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        queryset = RestaurantLocation.objects.all()
        
        return queryset
