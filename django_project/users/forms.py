from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


# To add an email field to our form (i.e. currently UserCreationForm):
class RegistrationForm(UserCreationForm):

    email = forms.EmailField()  # can add a `required=False`

    class Meta:
        """Configuration."""

        model = User  # class that'll be affected using this form
        fields = ['username', 'email', 'password1', 'password2']  # fields that'll be there in the form, and in this
        # order


# To update our user and profile, we're going to create some additional forms:
# A ModelForm allows us to create a form that will work with a specific database model, and in this case we want 2 forms
# that will update our User & Profile model.
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()  # can add a `required=False`

    class Meta:
        """Configuration."""

        model = User  # class that'll be affected using this form
        fields = ['username', 'email']  # fields that'll be there in the form, and in this order


# We need a different form to update profile pic because Profile is a different model than User.
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        """Configuration."""

        model = Profile  # class that'll be affected using this form
        fields = ['pic']  # fields that'll be there in the form, and in this order
