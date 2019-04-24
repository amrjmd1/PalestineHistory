from django.conf.urls import url, include
from Questions.views import *
from django.conf import settings
from django.conf.urls.static import static
from Client.views import *
from django.contrib import admin

urlpatterns = [
    # WebSite
    url(r'^$', MainPage.as_view(), name='MainPage'),

    # Dashboard
    url(r'^dashboard/admin_django/', admin.site.urls),
    url(r'^dashboard/', include('Dashboard.urls'), name='Dashboard'),

    # Client
    url(r'^user/', include('Client.urls'), name='Client'),

    # Client
    url(r'^user/', include('Video.urls'), name='Viedo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
