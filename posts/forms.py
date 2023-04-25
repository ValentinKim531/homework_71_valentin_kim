from django import forms
from django.contrib.auth import get_user_model

from posts.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            "image",
            "description",
        )

        labels = {
            "image": "Изображение",
            "description": "Описание",
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "text",
        )


