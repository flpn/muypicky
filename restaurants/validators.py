from django.core.exceptions import ValidationError


CATEGORIES = ['Pizzaria', 'Churrascaria', 'Sorveteria', 'Restaurante']

def validate_category(value):
    if not value.capitalize() in CATEGORIES:
        raise ValidationError("This category isn't allowed")
