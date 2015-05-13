from django.conf.urls import include, url
from tasks.views import *

urlpatterns = [
    url(r'^$', TaskList.as_view(), name='task_list'),
    url(r'^(?P<id>\d+)/$', TaskDetail.as_view(), name='task_detail'),
]
