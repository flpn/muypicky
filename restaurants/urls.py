from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
]
