from django.urls import *
from .views import *

urlpatterns = [
    path('userList/', userList, name='userList'),
]
