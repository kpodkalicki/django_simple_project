from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Topic(TitleSlugDescriptionModel, TimeStampedModel):

    def __str__(self):
        return self.title
