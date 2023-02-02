from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request=request, template_name='blog/home.html', context=context)
    # views always need to return either an `HttpResponse` or an `Exception`


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
