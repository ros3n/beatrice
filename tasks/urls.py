from django.conf.urls import include, url
from tasks.views import *

urlpatterns = (
    url(r'^$', TaskList.as_view(), name='task_list'),
    url(r'^(?P<id>\d+)/$', TaskDetail.as_view(), name='task_detail'),
    url(r'^categories/$', CategoryList.as_view(), name='task_list'),
    url(r'^categories/(?P<id>\d+)/$', CategoryDetail.as_view(), name='task_detail'),
    url(r'^notifications/$', NotificationList.as_view(), name='task_list'),
    url(r'^notifications/(?P<id>\d+)/$', NotificationDetail.as_view(), name='task_detail'),
)
