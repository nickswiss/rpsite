# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default='Blog', max_length=100),
        ),
    ]