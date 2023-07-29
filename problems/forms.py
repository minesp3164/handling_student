from django import forms
from .models import Comment, Problems


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


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = [
            'title',
            'difficulty',
            'content',
            'answer',
        ]
        widgets={
            "title": forms.TextInput(
                attrs={
                    "placeholder":"문제의 제목을 입력하여 주십시오.."
                },
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder":"문제를 입력하시오."
                },
            ),
            "difficulty": forms.Select(
                attrs={
                    "placeholder":"어렵기를 설정하시오."
                }
            ),
            "answer": forms.Select(
                attrs={
                    "placeholder":"정답을 입력하시오"
                }
            )
        }