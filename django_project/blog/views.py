from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


"""
def home(request):

    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }

    return render(request=request, template_name='blog/home.html', context=context)
    # views always need to return either an `HttpResponse` or an `Exception`
"""


# We can also directly pass the ListView.as_view(), and then passing the parameters that we want (in order to change the
# defaults), like we did for `LoginView`, `LogoutView`, if the changes are minor, but let's do it by extending the
# builtin Views and making changes in here.
class PostListView(ListView):

    model = Post  # which model to query to show the list

    template_name = 'blog/home.html'  # by default, it looks for f'{app_name}/{model_name}_{view_type}.html'
    # so, for current example, it's looking for 'blog/post_list.html', so we can configure the name
    # Btw, we've done this in the past too. (LoginView, LogoutView)

    context_object_name = 'posts'  # the variable name which will be used in the html code for looping over
    # by default, it's called `object`
    # Note that we can also change the names to defaults, then we won't need all these configurations.

    extra_context = {'title': 'Home'}

    ordering = ['-date_posted']  # show the objects in reverse order because we want the latest post to show on the top
    # that's how it should be, just think how would it be the other way around

    paginate_by = 5  # no. of posts to show on a single page


class PostDetailView(DetailView):

    model = Post  # which model to query to show the list


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post  # which model to query to show the list

    fields = ['title', 'content']  # fields which are going to be there in the form

    extra_context = {'heading': 'New Post'}  # not sure is this is the standard way or not, using for view-specific
    # heading and button text

    # Overriding in order to set the author:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post  # which model to query to show the list

    fields = ['title', 'content']  # fields which are going to be there in the form

    extra_context = {'heading': 'Edit Post'}  # not sure is this is the standard way or not, using for view-specific
    # heading and button text

    # UserPassesTestMixin: Deny a request with a permission error if the test_func() method returns False.
    def test_func(self):
        return self.request.user == self.get_object().author  # self.get_object(): will return current post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post  # which model to query to show the list

    success_url = '/'  # after successful deletion, redirection will be done to this url

    # UserPassesTestMixin: Deny a request with a permission error if the test_func() method returns False.
    def test_func(self):
        return self.request.user == self.get_object().author  # self.get_object(): will return current post


def about(request):

    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
