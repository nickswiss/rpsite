from __future__ import unicode_literals

from collections import namedtuple

from django.db import models
from django.contrib.auth.models import User

from photo.models import Photo, Album


PROFILE_PHOTOS_ALBUM = 'profile photos'


class Profile(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(blank=True)
    short_bio = models.CharField(max_length=200, blank=True)
    full_bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:
            self.profile_photo()  # Make sure there's a 'profile photos' album

        super(Profile, self).save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields
        )

    def profile_photo(self):
        filler = namedtuple('Album', 'image name')._make((
            'data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==',
            PROFILE_PHOTOS_ALBUM,
        ))

        try:
            album = Album.objects.get(user=self.user, name=PROFILE_PHOTOS_ALBUM)
            photo = album.primary_photo()
            return photo if photo else filler
        except Album.DoesNotExist:
            Album.objects.create(user=self.user, name=PROFILE_PHOTOS_ALBUM)
            return filler


class SocialMedia(models.Model):
    CHOICES = (
        ('github', 'github'),
        ('email', 'email'),
    )
    name = models.CharField(max_length=24, choices=CHOICES)
    data = models.CharField(max_length=64)
    user = models.ForeignKey(User)

    def __str__(self):
        return ' '.join((self.user.username, self.name))

    def icon(self):
        icons = {
            'github': 'github',
            'email': 'envelope'
        }
        return icons[self.name]
