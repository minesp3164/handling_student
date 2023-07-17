from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm


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
                login(request,user)
                return redirect('/problems/')
            else:
                print("aaaaa")
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


