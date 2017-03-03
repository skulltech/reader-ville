from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.name)


class Library(models.Model):
    user = models.OneToOneField(User)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    genre = models.ForeignKey('Genre', default=1)
    library = models.ForeignKey('Library')

    def __str__(self):
        return str(self.name)
