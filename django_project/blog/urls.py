from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]


# [Part 2 - Applications and Routes](https://youtu.be/a48xeeo5Vnk)
