from django.conf.urls import url
from Exam.views import *

app_name = 'Exam'

urlpatterns = [
    url(r'^$', ViewExams.as_view(), name='ViewExams'),
    url(r'^add/$', AddExam.as_view(), name='Add_Exam'),
    # url(r'^edit/$', EditExam.as_view(), name='Edit_Exam_Ajax'),
    # url(r'^remove/$', RemoveExam.as_view(), name='Remove_Exam_Ajax'),
]
