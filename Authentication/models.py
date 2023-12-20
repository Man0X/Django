from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pic = models.ImageField(
        upload_to='Auth/profile_pics/', blank=False, null=False, default='Auth/profile_pics/default.png')
    pass
