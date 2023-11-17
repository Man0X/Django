from django.shortcuts import render


def userList(request):
    return render(request, 'User/userList.html')
