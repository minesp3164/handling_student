from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'problem',
            'content',
        ]
        widgets={
            "content": forms.TextInput(
                attrs={
                    "placeholder":"댓글 달기.."
                }
            )
        }