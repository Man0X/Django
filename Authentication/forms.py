from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'profile_pic']

    def __init__(self, *args, user=None, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.user = user

        self.attrs = (
            {'class': 'Form', 'id': 'LoginForm'})

        self.fields['username'].widget.attrs.update(
            {'class': 'formField cblack', 'id': 'usernameField'})

        self.fields['password1'].widget.attrs.update(
            {'class': 'formField cblack', 'id': 'passwordField'})

        self.fields['password2'].widget.attrs.update(
            {'class': 'formField cblack', 'id': 'passwordField'})


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, user=None, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.user = user

        self.attrs = (
            {'class': 'Form', 'id': 'LoginForm'})

        self.fields['username'].widget.attrs.update(
            {'class': 'formField cblack', 'id': 'usernameField'})

        self.fields['password'].widget.attrs.update(
            {'class': 'formField cblack', 'id': 'passwordField'})
