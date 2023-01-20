from django.shortcuts import render


# Create your views here.


posts = [
    {
        'title': 'Post 1',
        'author': 'Samyak Jain',
        'date': '13 January 2023',
        'content': 'This is my first blog post.'
    },
    {
        'title': 'Post 2',
        'author': 'Samyak Jain',
        'date': '13 January 2023',
        'content': 'This is my second blog post.'
    }
]  # let's just pretend for now that we made a database call and got back this list of posts, and we want to display
# these posts on our blog homepage


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request=request, template_name='blog/home.html', context=context)
    # views always need to return either an `HttpResponse` or an `Exception`
    # [Part 3 - Templates](https://youtu.be/qDwdMDQ8oX4)


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
