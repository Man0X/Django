from django.shortcuts import render
from .models import User


def login(request):
    return render(request, 'Authentication/login.html')


def userList(request):
    context = {
        'Users': User.objects.all()
    }
    return render(request, 'Authentication/userList.html', context)
