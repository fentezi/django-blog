from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, FormView, ListView
from blog import models
from . import forms


# Create your views here.
class HomeTemplateView(ListView):
    model = models.BlogCreateModel
    queryset = models.BlogCreateModel.objects.all().order_by('-created_at')[:3]
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email_form'] = forms.EmailForm()
        return context


class EmailSendView(FormView):
    form_class = forms.EmailForm
    template_name = 'pages/index.html'
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'


class ContactTemplateView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email_form'] = forms.EmailForm()
        return context
