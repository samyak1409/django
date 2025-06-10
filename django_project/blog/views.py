from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse


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

    # extra_context = {'title': f'All Posts ({Post.objects.count()})'}
    # Problem: Post count not updating
    # Reason: Evaluated once at the time the view is initialized, not again on each request
    # Solution: Override `get_context_data()`
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Since `UserPostListView` & `PostDetailView` are child CBVs of current CBV, and we're not overriding
        # `get_context_data` again in those CBVs, this `get_context_data` method only would be used there as well.
        # And since, we don't want to set 'title' to `f'All Posts ({Post.objects.count()})'` for those views, adding the
        # condition:
        if 'title' not in context:
            context['title'] = f'All Posts ({Post.objects.count()})'
            # `Post.objects.count()`:
            # - Most efficient: Performs a SELECT COUNT(*) SQL query directly in the database.
            # - Returns an integer.
            # - Doesn't fetch any rows, just the count.
        return context
    # Approach; When is it evaluated?; Per request?
    # `extra_context = { ... }`; Once (on class load); No
    # `get_context_data()` override; Every time view is called; Yes
    # Function-based view context; Every time view is called; Yes
    # [Ref: https://chatgpt.com/share/683cd2a0-929c-800a-bf9f-32079aeadc28]

    ordering = ['-time_posted']  # show the objects in reverse order because we want the latest post to show on the top
    # that's how it should be, just think how would it be the other way around

    paginate_by = 5  # no. of posts to show on a single page


class UserPostListView(PostListView):

    # Overriding:
    def get_queryset(self):

        username = self.kwargs.get('username')  # username of user whose posts needs to be shown
        user = get_object_or_404(klass=User, username=username)  # user (object) whose posts needs to be shown
        # `get_object_or_404` will raise 404 if user with this username doesn't exist.
        filtered_posts = Post.objects.filter(author=user)
        # user_posts = user.post_set.all()  # this can also be used; `post_set`: auto created field by django

        # For Page Title:
        if user == self.request.user:  # if user whose posts needs to be shown is current logged-in user
            title = f'Your Posts'
        else:
            title = f'Posts by {username}'
        self.extra_context = {'title': f'{title} ({filtered_posts.count()})'}

        return filtered_posts.order_by('-time_posted')


class PostDetailView(PostListView):

    # Reset:
    extra_context = {'title': None}
    # (`'title': None` so that `PostListView.get_context_data` works correctly without needing to override here)
    paginate_by = None

    # Overriding:
    def get_queryset(self):
        return [get_object_or_404(klass=Post, pk=self.kwargs.get('pk'))]
        # `get_object_or_404` will raise 404 if post with this pk doesn't exist.
        # returning as a list because `get_queryset` must return an iterable.


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

    return render(request=request, template_name='blog/about.html', context={'title': 'Project Highlights'})


def wake_up(request):
    """
    When someone visits my portfolio (samyak1409.github.io),
    a GET request is sent here to wake prod server from sleep (because free tier),
    improving UX for real visitors.
    """
    # We can add logging here to track wake-up pings.
    print('Wake-up ping received!')
    return JsonResponse({'status': 'awake'})
