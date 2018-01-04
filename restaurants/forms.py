from django import forms

from .models import RestaurantLocation


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=True)
    category = forms.CharField(required=True)


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = ['name', 'location', 'category',]
