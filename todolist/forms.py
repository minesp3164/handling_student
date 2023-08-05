from django import forms

from .models import TodoList


class TodoListForm(forms.ModelForm):
    class Meta:
      model = TodoList
      fields = [
        'title',
        'content',
        'finish_at',
      ]

      widgets={
        'title': forms.TextInput(
          attrs={
            "placeholder":"제목.."
          }
        ),
        "content": forms.TextInput(
          attrs={
            "placeholder":"할일.."
          }
        ),
        "finish_at": forms.DateInput(),
      }