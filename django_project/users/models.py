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
    # `default`: Not making it compulsory to upload a profile pic, so if the user doesn't upload one, this default pic
    #            will be used.
    # `upload_to`: Dir in which the profile pics will be saved.

    # (You should already know what the following is for.)
    def __str__(self):
        return f'{self.user.username} Profile'

    # Override save method in order to resize whenever a large pic is uploaded (to save space):
    def save(self, *args, **kwargs):

        # If `pic` is newly selected pic and not Default/Old one:
        if not self.pic.name.startswith('Profile Pics/'):

            # Get the current profile pic (the one before updating):
            curr_pic = Profile.objects.get(pk=self.pk).pic
            # Delete it if it's not the Default one:
            if curr_pic.name != 'Profile Pics/Default.jpg':
                curr_pic.delete(save=False)
                # `save=False` so that if while saving the new pic below, some error occur, we don't lose the current
                # one

            # Change the name of new pic to save as 'user_id.ext':
            self.pic.name = f'{self.user.id}.{self.pic.name.split(".")[-1]}'
            # `self.pic.name.split(".")[-1]`: extension must be the same.

        # Call the parent `save` which saves the pic:
        super().save(*args, **kwargs)

        # Compressing the img for saving space:
        with Image.open(fp=self.pic.path) as img:
            changed = False
            # First, square crop if required:
            # https://stackoverflow.com/questions/16646183/crop-an-image-in-the-centre-using-pil
            w, h = img.size
            min_ = min(w, h)
            if w != h:
                img = img.crop(box=((w-min_)//2, (h-min_)//2, (w+min_)//2, (h+min_)//2))  # crop in center
                changed = True
            # Then, compress if required:
            if min_ > (dim := 720):
                img.thumbnail(size=(dim, dim))
                changed = True
            # Overwrite to the same path if changed:
            if changed:
                img.save(fp=self.pic.path)
