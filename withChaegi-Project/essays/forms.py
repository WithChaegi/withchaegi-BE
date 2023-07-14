from django import forms
from .models import Essay, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('essay', 'user',)