from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Topic(MPTTModel, TitleSlugDescriptionModel, TimeStampedModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    is_public = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title