from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    return render(request=request, template_name='users/register.html', context={'form': UserCreationForm()})
