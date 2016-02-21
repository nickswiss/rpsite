from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Blog(models.Model):
    user = models.OneToOneField(User)


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog)
    name = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

