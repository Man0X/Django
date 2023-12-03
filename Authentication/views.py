from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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

    form = AuthenticationForm()
    context = {
        "loginForm": form
    }
    return render(request, "Authentication/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    if request.method == 'POST':
        registerForm = UserCreationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save()

            username = registerForm.cleaned_data['username']
            password = registerForm.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        registerForm = UserCreationForm()

    registerForm.fields['username'].help_text = None
    # registerForm.fields['password1'].help_text = ''
    # registerForm.fields['password2'].help_text = ''

    context = {'registerForm': registerForm}
    return render(request, 'Authentication/register.html', context)


def userList(request):
    userModel = get_user_model()
    context = {
        'Users': userModel.objects.all()
    }
    return render(request, 'Authentication/userList.html', context)
