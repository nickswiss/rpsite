from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('include/mini_bio.html')
def mini_bio(profile):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'profile': profile
    }
