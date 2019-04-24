from django.conf.urls import url
from Event.views import *

app_name = 'Event'

urlpatterns = [
    url(r'^$', ViewEvent.as_view(), name='ViewEvent'),
    url(r'^addevent/$', ViewAddEvent.as_view(), name='addeventshow'),
    url(r'^add/$', AddEvent.as_view(), name='Add_Event_Ajax'),
    url(r'^edit/$', EditEvent.as_view(), name='Edit_Event_Ajax'),
    url(r'^remove/$', RemoveEvent.as_view(), name='Remove_Event_Ajax'),
]
