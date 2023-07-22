from django.contrib import admin

from .models import Problems, Answer, Difficulty, Comment

admin.site.register(Problems)
admin.site.register(Answer)
admin.site.register(Difficulty)
admin.site.register(Comment)