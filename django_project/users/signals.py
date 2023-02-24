"""
https://github.com/samyak1409/django#5-using-signals-set-to-auto-create-the-profile-with-the-default-profile-pic-whenever-a-new-user-is-created
"""


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
