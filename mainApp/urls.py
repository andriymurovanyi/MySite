# Created by hiddencoder at 03.03.2019

from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
]

