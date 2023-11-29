from django.contrib import admin
from django.urls import *

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', include("Authentication.urls"))
]
