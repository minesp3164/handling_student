from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import TodoList


def todolist_view(request):
    todolists = TodoList.objects.filter(author=request.user)

    context = {
        "todolists": todolists
    }

    return render(request, 'todolist/todolist_list.html', context)

def todolist_add(request):
    pass

def todolist_detail(request,todolist_id):

    todolist = TodoList.objects.get(id=todolist_id)
    return render(request, 'todolist/todolist_detail.html',{"todolist":todolist})


def todolist_checked(request, todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)

    if todolist.checked:
        todolist.checked = False
    else:
        todolist.checked = True
    todolist.save()

    return HttpResponseRedirect("/todolist/")