from django.db import models


class TodoList(models.Model):
    content = models.CharField(max_length=250)
    checked = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    edited_at = models.DateField(auto_now_add=True)
    finish_at = models.DateField(null=True)
    author = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)

    def __str__(self):
        return self.content
