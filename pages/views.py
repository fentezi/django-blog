from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'pages/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'


class ContactTemplateView(TemplateView):
    template_name = 'pages/contact.html'
