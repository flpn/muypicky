from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .forms import ItemForm


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
    model = Item


class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = 'menus/item_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user

        return super(ItemCreateView, self).form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Item'
        
        return context

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        
        return kwargs


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ItemForm
    template_name = 'menus/item_detail.html'
    model = Item

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user

        return super(ItemUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'

        return context

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs
