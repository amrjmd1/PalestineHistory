from django.conf.urls import url
from Category.views import *

app_name = 'Category'

urlpatterns = [
    url(r'^$', ViewCategories.as_view(), name='ViewCategories'),
    url(r'^(?P<category_id>[0-9]+)/$', ViewCategory.as_view(), name='ViewCategory'),
    url(r'^(?P<category_id>[0-9]+)/question/$', QuestionCategory.as_view(), name='QuestionCategory'),
    url(r'^add/$', AddCategory.as_view(), name='Add_Category'),
    url(r'^add/ajax$', AddCategoryAjax.as_view(), name='Add_Category_Ajax'),
    url(r'^edit/$', EditCategory.as_view(), name='Edit_Category_Ajax'),
    url(r'^remove/$', RemoveCategory.as_view(), name='Remove_Category_Ajax'),
]
