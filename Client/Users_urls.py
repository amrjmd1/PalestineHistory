from django.conf.urls import url
from .views import *

app_name = 'Users'

urlpatterns = [
    url(r'^$', ViewUsers.as_view(), name='ViewUsers'),
    url(r'^add/$', AddUser.as_view(), name='AddUser'),
    url(r'^remove/$', RemoveUser.as_view(), name='Remove_User_Ajax'),
    url(r'^edit/$', EditUser.as_view(), name='Edit_User_Ajax'),
]
