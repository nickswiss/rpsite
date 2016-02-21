from django import template
from django.conf import settings

from home.models import SocialMedia

register = template.Library()


@register.inclusion_tag('include/mini_bio.html')
def mini_bio(profile):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'profile': profile
    }

@register.inclusion_tag('include/social_media_links.html')
def social_media_links(user):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'social_media': SocialMedia.objects.filter(user=user)
    }
