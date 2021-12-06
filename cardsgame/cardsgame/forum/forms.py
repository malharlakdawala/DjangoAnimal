from django import forms
from .models import Forum_post, Comment_post


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Forum_post
        exclude = ['date_created', 'forum_post_author']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment_post
        exclude = ['comment_author', 'forum']
