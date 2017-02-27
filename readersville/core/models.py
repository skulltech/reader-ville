from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return str(self.name)

class Author(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=500, blank=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	bio = models.TextField(max_length=500, blank=True)
	genres = models.ManyToManyField(Genre)

# Methods to link the User and UserProfile models

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()