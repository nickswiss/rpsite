from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView

from .forms import BlogPostForm
from .models import BlogPost


class Blog(CreateView):

    template_name = 'blog.html'
    form_class = BlogPostForm
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        
        return context
