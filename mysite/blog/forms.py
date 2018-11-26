from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('workout_name', 'text', 'rep_amount', 'set_amount',)
