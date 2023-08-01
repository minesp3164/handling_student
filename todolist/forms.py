from django import forms

from .models import TodoList


class TodoListForm(forms.ModelForm):
    class Meta:
      model = TodoList
      fields = [
        'content',
        'finish_at',
      ]

      widgets={
        "content": forms.TextInput(
          attrs={
            "placeholeder":"할일.."
          }
        ),
        "finish_at": forms.DateInput()
      }