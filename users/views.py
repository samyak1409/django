from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):

    if request.method == 'POST':  # when submit button is pressed

        form = RegistrationForm(data=request.POST)  # creates a form with the existing data, the data which is in the
        # request

        if form.is_valid():
            form.save()  # save the inputted data to the DB
            messages.success(request=request,
                             message=f'Account created for {form.cleaned_data.get("username")}, now you can log in.')
            return redirect(to='login')

    else:
        form = RegistrationForm()  # creates an empty form

    return render(request=request, template_name='users/register.html', context={'form': form})


@login_required
def profile(request):

    # For updating the username/email/pic:
    if request.method == 'POST':  # when submit button is pressed

        u_form = UserUpdateForm(data=request.POST, instance=request.user)
        p_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        # `request.FILES`: for image

        if u_form.is_valid() and p_form.is_valid():
            u_form.save(), p_form.save()  # save the inputted data to the DB
            messages.success(request=request, message=f'Your account has been updated successfully!')
            return redirect(to='profile')  # This is imp here too because of something called the post get redirect
            # pattern. If you've ever reloaded your browser after submitting a form, a weird message comes up sometimes
            # that says data will be resubmitted. That is your browser telling you that you're about to run another post
            # request if you reload your page. So, us redirecting here causes the browser to send a get request, and
            # then we don't get that weird message if we reload.

    # Get Request:
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request=request, template_name='users/profile.html', context={'u_form': u_form, 'p_form': p_form})
