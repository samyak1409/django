from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# To add an email field to our form (i.e. currently UserCreationForm):
class RegistrationForm(UserCreationForm):

    email = forms.EmailField()  # can add a `required=False`

    class Meta:
        """Configuration."""

        model = User  # class that'll be affected using this form
        fields = ['username', 'email', 'password1', 'password2']  # fields that'll be there in the form, and in this
        # order
