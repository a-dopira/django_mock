from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    notes = models.ManyToManyField(Note, related_name='categories')
