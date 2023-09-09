from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, DetailView,
                                  UpdateView, DeleteView, TemplateView)

from . import models


# Create your views here.
class BlogView(ListView):
    model = models.BlogCreateModel
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = models.BlogCreateModel
    template_name = 'blog/detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
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


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.BlogCreateModel
    fields = (
        'image',
        'title',
        'body',
    )
    template_name = 'blog/update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(DeleteView):
    model = models.BlogCreateModel
    success_url = reverse_lazy('blog:blog_home')
    template_name = 'blog/delete.html'
