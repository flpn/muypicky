from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.RestaurantsListView.as_view(), name='restaurants'),
    path('create/', views.RestaurantCreateView.as_view(), name='create'),
    path('<slug:slug>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
]
