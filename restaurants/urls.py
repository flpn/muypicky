from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.RestaurantsListView.as_view(), name='restaurants'),
    path('<str:slug>/', views.RestaurantsListView.as_view(), name='restaurants_search'),
]
