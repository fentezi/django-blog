from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
]