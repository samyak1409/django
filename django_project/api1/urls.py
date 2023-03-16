from django.urls import path
from .views import available_endpoints


urlpatterns = [
    path('', available_endpoints),
]
