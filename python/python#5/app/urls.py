from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('app/', views.index),
    path('reg/', views.index),
    path('photo/', views.photo)
]
