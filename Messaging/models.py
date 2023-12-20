from django.db import models
from Authentication.models import User


class Message(models.Model):
    content = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
