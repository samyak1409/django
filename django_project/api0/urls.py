from django.urls import path
from .views import get_endpoints


urlpatterns = [
    path('', get_endpoints)
]
