from django.contrib import admin
from django.urls import *

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('user/', include('User.urls'))
]
