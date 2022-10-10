from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'postCategory', 'title', 'text']
