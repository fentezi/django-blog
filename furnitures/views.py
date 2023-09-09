from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models


# Create your views here.
class FurnitureView(ListView):
    model = models.FurnituresModel
    template_name = 'furnitures/furnitures.html'


class FurnitureCreateView(CreateView):
    model = models.FurnituresModel
    fields = '__all__'
    template_name = 'furnitures/furniture_create.html'
