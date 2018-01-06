from django.urls import path
from . import views


app_name = 'menus'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='items'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('<int:pk>/edit', views.ItemUpdateView.as_view(), name='item_update'),
    path('create/', views.ItemCreateView.as_view(), name='create'),
]