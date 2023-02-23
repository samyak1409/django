from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Extend the `User` model, in order to be able to add a profile image field:
class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    # `on_delete=models.CASCADE`: delete this profile if the user is deleted.

    pic = models.ImageField(default='Default Profile Pic.jpg', upload_to='Profile Pics')

    def __str__(self):
        return f'{self.user.username} Profile'
