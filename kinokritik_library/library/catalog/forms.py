from django import forms
from django.forms import ModelForm
from .models import Comment, Rating


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        labels = {'comment_text': ''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in ['comment_text']:
            self.fields[field].help_text = None
        self.fields['comment_text'].widget = forms.Textarea(attrs={'placeholder': 'Написать отзыв', 'rows': 5})


class RatingForm(ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Rating
        fields = ['rating']
        labels = {'rating': ''}

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in ['rating']:
            self.fields[field].help_text = None
