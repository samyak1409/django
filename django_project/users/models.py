from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


# Extend the `User` model, in order to be able to add a profile image field:
class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    # `OneToOneField`: Similar to `ForeignKey`.
    # `on_delete=models.CASCADE`: Delete this profile if the user is deleted.

    pic = models.ImageField(default='Profile Pics/Default.jpg', upload_to='Profile Pics')
    # `default`: Not making it compulsory to upload a profile pic, so if the user don't upload one, this default pic
    #            will be used.
    # `upload_to`: Dir in which the profile pics will be saved.

    # (You should already know what the following is for.)
    def __str__(self):
        return f'{self.user.username} Profile'

    # Override save method in order to resize whenever a large pic is uploaded (to save space):
    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)  # call the parent's `save` method which saves the pic

        img = Image.open(self.pic.path)  # then open the pic
        if img.width > 720 or img.height > 720:  # check size, if big:
            img.thumbnail(size=(720, 720))  # resize
            img.save(self.pic.path)  # overwrite to the same path
