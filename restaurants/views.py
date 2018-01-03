from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import RestaurantLocation

# Create your views here.
class RestaurantsListView(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')

        if not slug:
            queryset = RestaurantLocation.objects.all()
        else:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        
        return queryset


class RestaurantDetailView(DetailView):
    template_name = 'restaurants/restaurant_detail.html'
    model = RestaurantLocation
    
