from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    # path('', views.home, name='home'),  # function view
    path('', PostListView.as_view(), name='home'),  # class-based view

    path('about/', views.about, name='about'),
]
