from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # creates a form with the existing data, the data which is in the request
        if form.is_valid():
            form.save()  # save the inputted data to the DB
            messages.success(request=request, message=f'Account created for {form.cleaned_data.get("username")}!')
            return redirect(to='home')
    else:
        form = UserCreationForm()  # creates an empty form

    return render(request=request, template_name='users/register.html', context={'form': form})
