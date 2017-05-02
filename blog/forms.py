"""Configuration for project's forms."""

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Configuration for Post form."""

    class Meta:
        model = Post
        fields = ('title', 'text',)
