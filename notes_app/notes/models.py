from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    notes = models.ManyToManyField(Note, related_name='categories')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories_list', kwargs={'category_slug': self.slug})
