from django.contrib import admin
from django.urls import *

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('', home, name='home'),
    path('auth/', include("Authentication.urls"))
]
