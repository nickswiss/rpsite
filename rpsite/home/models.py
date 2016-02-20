from __future__ import unicode_literals

from collections import namedtuple

from django.db import models
from django.contrib.auth.models import User

from photo.models import Photo, Album


class Profile(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(blank=True)
    short_bio = models.CharField(max_length=200, blank=True)
    full_bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def profile_photo(self):
        album_name = 'profile photos'
        filler = namedtuple('Album', 'image name')._make((
            'data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==',
            album_name,
        ))

        try:
            album = Album.objects.get(user=self.user, name=album_name)
            photo = album.primary_photo()
            if photo:
                return photo
            else:
                return filler
        except Album.DoesNotExist:
            Album.objects.create(user=self.user, name=album_name)
            return filler
