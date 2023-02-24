from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Extend the `User` model, in order to be able to add a profile image field:
class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    # `OneToOneField`: Similar to `ForeignKey`.
    # `on_delete=models.CASCADE`: Delete this profile if the user is deleted.

    pic = models.ImageField(default='Default Profile Pic.jpg', upload_to='Profile Pics')
    # `default`: Not making it compulsory to upload a profile pic, so if the user don't upload one, this default pic
    #            will be used.
    # `upload_to`: Dir in which the profile pics will be saved.

    # (You should already know what the following is for.)
    def __str__(self):
        return f'{self.user.username} Profile'
