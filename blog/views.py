from django.core.files.base import ContentFile
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from . import models


# Create your views here.
class BlogView(ListView):
    model = models.BlogCreateModel
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = models.BlogCreateModel
    template_name = 'blog/detail.html'


class BlogCreateView(CreateView):
    model = models.BlogCreateModel
    fields = (
        'image',
        'title',
        'body',
    )
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
