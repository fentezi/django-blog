from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog_home'),
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/update/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('<slug:slug>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
