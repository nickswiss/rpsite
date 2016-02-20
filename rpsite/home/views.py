from django.views.generic.base import TemplateView

from home.models import Profile


class Homepage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        context['profiles'] = Profile.objects.filter(user__is_staff=True)
        return context
