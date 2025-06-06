from django.urls import path
from .views import available_endpoints, all_posts, single_post, posts_by_a_user


urlpatterns = [
    path('', available_endpoints, name='api1'),
    path('posts/', all_posts),
    path('posts/<int:pk>/', single_post),
    path('posts/by/<str:username>/', posts_by_a_user),
]
