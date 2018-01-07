from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm


class RestaurantsListView(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(DetailView):
    template_name = 'restaurants/restaurant_detail.html'
    model = RestaurantLocation
    

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/create_restaurant_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user

        return super(RestaurantCreateView, self).form_valid(form)
