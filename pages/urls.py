from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('send_email/', views.EmailSendView.as_view(), name='send_email'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
]
