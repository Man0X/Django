from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    username = models.CharField(
        unique=True, blank=False, default='username', max_length=50)
    password = models.CharField(
        unique=True, blank=False, default='password', max_length=100)
    email = models.EmailField(unique=True)
