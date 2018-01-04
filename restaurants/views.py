from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm


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
    

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/create_restaurant_form.html'
    success_url = '/restaurants/'
