from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Create your views here.


@api_view(http_method_names=['GET'])
def available_endpoints(request):

    endpoints = {'Get all Posts': 'GET /posts/',
                 'Get a single Post': 'GET /posts/:id/',
                 'Get all Posts by a particular User': 'GET /posts/by/:username/'}
    return Response(data=endpoints)


@api_view(http_method_names=['GET'])
def all_posts(request):

    # posts = Post.objects.all()
    # return Response(data=posts)
    # TypeError: Object of type Post is not JSON serializable

    posts = PostSerializer(Post.objects.all(), many=True).data
    # `many=True`: tell that it's going to be an iterable of objects, not a single object
    return Response(data=posts)


@api_view(http_method_names=['GET'])
def single_post(request, pk):

    # post = PostSerializer(Post.objects.get(pk=pk)).data
    # Raise 404 with post id which doesn't exist:
    post = PostSerializer(get_object_or_404(klass=Post, pk=pk)).data
    return Response(data=post)


@api_view(http_method_names=['GET'])
def posts_by_a_user(request, username):

    # First, we have to get the `user` by `username` (because `author` is linked by `ForeignKey` to `User`):
    user = get_object_or_404(klass=User, username=username)
    # Now, we can use this `user` to filter the posts:
    posts = PostSerializer(Post.objects.filter(author=user), many=True).data
    # `many=True`: tell that it's going to be an iterable of objects, not a single object
    return Response(data=posts)
