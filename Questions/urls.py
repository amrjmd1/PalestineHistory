from django.conf.urls import url
from Questions.views import *

app_name = 'Questions'

urlpatterns = [
    url(r'^$', ViewQuestions.as_view(), name='ViewQuestions'),
    url(r'^upload_excel$', UploadFiles.as_view(), name='UploadFiles'),
    url(r'^excel/upload_files/$', UploadExcel.as_view(), name='Upload_Excel_Ajax'),
]
