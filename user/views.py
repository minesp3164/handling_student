from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import LoginForm, SignupForm, UserForm
from .models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/problems/")
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user:
                login(request, user)
                return redirect('/problems/')
            else:
                form.add_error(None,"입력한 자격증명에 해당되는 사용자가 없습니다.")
        context = {
            "form": form,
        }
        return render(request, "user/user_login.html", context)
    else:
        form = LoginForm()
        context = {
            "form": form,
        }
        return render(request, "user/user_login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/user/login/")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/problems/")
        else:
            context = {
                "form": form,
            }
            return render(request, "user/user_signup.html",context)
    else:
        form = SignupForm()
        context = {
            "form": form
        }
        return render(request, "user/user_signup.html", context)


def user_detail(request,username):
    user = User.objects.get(username=username)
    last_login = timezone.now() - user.last_login
    ismin = False
    if last_login.seconds > 60:
        last_login = last_login.seconds//60
        ismin = True

    context = {
        'user': user,
        'lastlogin':last_login,
        'ismin': ismin
    }
    return render(request, "user/user_detail.html", context)


def user_edit(request,username):
    user = get_object_or_404(User,username=username)
    if user != request.user:
        messages.error(request,'이 아이디의 주인이 아닙니다')
        return redirect('/problems/')
    if request.method == "POST":
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect(f'/user/detail/{user.username}')
        else:
            form.add_error("모든 것을 채우시오.")
    else:
        form = UserForm(instance=user)
    context = {
        "form":form
    }
    return render(request,'user/user_edit.html',context)


