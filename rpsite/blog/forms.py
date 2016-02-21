from django import forms
from .models import BlogPost


class BlogPostForm(forms.models.ModelForm):

    class Meta:

        model = BlogPost
        fields = ('name', 'content', 'blog',)

        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Post Name',
                'class': 'form-control input-lg',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Content',
                'class': 'form-control',
            }),
        }
