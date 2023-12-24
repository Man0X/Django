from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import *
from .models import *
from .forms import UserRegisterForm, UserLoginForm


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Identifiants incorrects')

    form = UserLoginForm()
    context = {
        "loginForm": form
    }
    return render(request, "Authentication/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    if request.method == 'POST':
        registerForm = UserRegisterForm(request.POST, request.FILES)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.set_password(registerForm.cleaned_data['password1'])
            profile_pic = registerForm.cleaned_data.get('profile_pic')

            user.save()
            login(request, user)
            return redirect('home')
    else:
        registerForm = UserRegisterForm()

    context = {'registerForm': registerForm}
    return render(request, 'Authentication/register.html', context)


@login_required()
def userList(request):
    context = {
        'Users': User.objects.all()
    }
    return render(request, 'Authentication/userList.html', context)
