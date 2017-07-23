__author__ = 'szandala'

from django.forms import ModelForm
from myself.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'body')