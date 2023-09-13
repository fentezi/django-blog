from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models
from cart import forms


# Create your views here.
class FurnitureView(ListView):
    model = models.FurnituresModel
    template_name = 'furnitures/furnitures.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = forms.CartForm(initial={
            'quantity': 1,
        })
        return context


class FurnitureCreateView(CreateView):
    model = models.FurnituresModel
    fields = '__all__'
    template_name = 'furnitures/furniture_create.html'
