from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    if request.method == 'POST':
        message_creation_form = MessageCreationForm(
            request.POST, user=request.user)
        if message_creation_form.is_valid():
            message_creation_form.save()
            return redirect('messagingHome')
    else:
        message_creation_form = MessageCreationForm(user=request.user)

    context = {
        'MessageCreationForm': message_creation_form,
        'Messages': Message.objects.all()
    }
    return render(request, 'Messaging/home.html', context)
