from django.urls import path
from . import views
from .views import PostListView, PostDetailView

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

    path('about/', views.about, name='about'),
]
