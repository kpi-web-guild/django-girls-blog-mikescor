"""This module keeps the collection of form declarations representing HTML forms."""

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for Post model."""

    class Meta:
        model = Post
        fields = ('title', 'text',)
