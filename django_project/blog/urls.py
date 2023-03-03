from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.home, name='home'),  # function view
    path('', PostListView.as_view(), name='home'),  # class-based view

    path('post/<int:pk>/', PostDetailView.as_view(), name='read'),
    # now, this is something we're using first time, defining variable inside an url pattern
    # so, what's going to happen is:
    # 1) we'll access the DetailView (i.e. read a post) by going to the page /post/post_id
    # 2) then, django will check matching url pattern, and here this url pattern will be matched, so, <int: pk> is
    # basically we're declaring a var, which will input the val, "int: " part is optional, and "pk" is the default var
    # name DetailView expects
    # 3) then, pk var is passed into our PostDetailView, and then the particular post is rendered on the page.
    # Simple!

    path('post/new/', PostCreateView.as_view(), name='create'),
    # template_name: you might think that for this one it should be post_create, but this one will actually share a
    # template with the UpdateView, so Django expect this template to be the name f'{model_name}_form'

    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),

    path('about/', views.about, name='about'),
]
