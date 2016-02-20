from __future__ import unicode_literals
from os import path
import six

from django.contrib.auth.models import User
from django.db import models


class Album(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return ' '.join((self.user.username, self.name), )

    def primary_photo(self):
        return self.photo_set.filter(primary=True).first()


def photo_upload_to(instance, filename):
    return path.join(
        six.text_type(instance.album.user.id),
        'photos',
        six.text_type(instance.album.id),
        filename
    )


class Photo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey('Album')
    primary = models.BooleanField(default=False)
    name = models.CharField(max_length=32, unique=True)
    image = models.ImageField(upload_to=photo_upload_to)

    def __str__(self):
        return self.name
