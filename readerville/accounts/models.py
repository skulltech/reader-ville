from django.db import models
from django.contrib.auth.models import User
from libraries.models import Genre

from django.db.models.signals import post_save
from django.dispatch import receiver


class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=500, blank=True)
    genres = models.ManyToManyField(Genre)
    location = models.ForeignKey(Location, blank=True, null=True)

    def __str__(self):
        return str(self.name)


# Methods to link the User and UserProfile models

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
