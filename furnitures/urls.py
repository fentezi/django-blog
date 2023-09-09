from django.urls import path
from . import views

app_name = 'furnitures'

urlpatterns = [
    path('', views.FurnitureView.as_view(), name='furn_main'),
    path('create/', views.FurnitureCreateView.as_view(), name='furn_create'),
]
