from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

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


def todolist_delete(request,todolist_id):
    todolist = get_object_or_404(TodoList,pk=todolist_id)
    if todolist.author == request.user:
        todolist.delete()
    return HttpResponseRedirect("/todolist/")


def todolist_edit(request, todolist_id):
    todolist = get_object_or_404(TodoList,pk=todolist_id)
    if request.user != todolist.author:
        messages.error(request, '수정 권한이 없습니다!')
        return redirect('/todolist/')
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todolist)
        if form.is_valid():
            todolist = form.save(commit=False)
            todolist.edited_at = timezone.now()
            todolist.save()
            return HttpResponseRedirect(f'/todolist/detail/{todolist.id}')
        else:
            form.add_error("모든 것을 채우시오")
    else:
        form = TodoListForm(instance=todolist)
    context = {
        "form": form
    }
    return render(request,'todolist/todolist_edit.html',context)