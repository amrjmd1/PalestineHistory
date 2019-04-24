from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from Dashboard.views import *


app_name = 'Dashboard'

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='HomePage'),

    url(r'^login$', LoginDashboard.as_view(), name='login'),
    url(r'^authentication/$', CheckLoginDashboard.as_view(), name='Login_Form_Ajax'),
    url(r'^logout_user/(?P<session_user>[\w-]+)/$', LogoutDashboard.as_view(), name='logoutDashboard'),
    url(r'^questions/', include('Questions.urls')),
    url(r'^category/', include('Category.urls')),
    url(r'^events/', include('Event.urls')),
    url(r'^exams/', include('Exam.urls')),
    url(r'^users/', include('Client.Users_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
