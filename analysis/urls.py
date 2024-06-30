from django.urls import path
from . import views
import os

urlpatterns = [
    path('', views.josaa, name='josaa'),
    path('Institute_neutral/', views.Institute_neutral, name='Institute_neutral'),
    path('Institute_female/', views.Institute_female, name='Institute_female'),
    path('Branch_neutral/', views.Branch_neutral, name='Branch_neutral'),
    path('Branch_female/', views.Branch_female, name='Branch_female'),
    
]



