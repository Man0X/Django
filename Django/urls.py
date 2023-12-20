from django.contrib import admin
from django.urls import *
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('', home, name='home'),
    path('auth/', include('Authentication.urls')),
    path('messaging/', include('Messaging.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
