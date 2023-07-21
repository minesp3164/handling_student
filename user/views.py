from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
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
        return render(request, "user/login.html", context)
    else:
        form = LoginForm()
        context = {
            "form": form,
        }
        return render(request, "user/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/user/login/")


def signup_view(request):
    if request.method=="POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 != password2:
                form.add_error("password2", "비밀번호와 비밀번호 확인란의 값이 다릅니다.")
            if User.objects.filter(username=username).exists():
                form.add_error("username", "입력한 사용자명은 이미 사용중입니다.")
            if form.errors:
                context = {"form": form}
                return render(request, "user/signup.html", context)
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                )
                login(request, user)
                return redirect('/problems/')
    else:
        form = SignupForm()
        context = {
            "form": form
        }
        return render(request, "user/signup.html", context)
