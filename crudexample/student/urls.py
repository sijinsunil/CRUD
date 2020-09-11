from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home,name='home'),
    path('update/<int:id>/', views.update, name='updatedata'),
    path('delete/<int:pk>/', views.delete, name='deletedata'),
    
]

