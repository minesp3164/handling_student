from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TodoListForm
from .models import TodoList


def todolist_view(request):
    todolists = TodoList.objects.filter(author=request.user)

    context = {
        "todolists": todolists
    }

    return render(request, 'todolist/todolist_list.html', context)


def todolist_add(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit=False)
            todolist.author = request.user

            todolist.save()

            return HttpResponseRedirect('/todolist/')
    else:
        form = TodoListForm()
    context = {"form":form}
    return render(request,'todolist/todolist_add.html', context)


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