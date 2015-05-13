from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )
from tasks.models import Task, Category, Notification
from tasks.serializers import (
    TaskSerializer, CategorySerializer, NotificationSerializer)


class TaskMixin(object):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskList(TaskMixin, ListCreateAPIView):
    pass


class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
    pass


class CategoryMixin(object):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(CategoryMixin, ListCreateAPIView):
    pass


class CategoryDetail(CategoryMixin, RetrieveUpdateDestroyAPIView):
    pass


class NotificationMixin(object):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationList(NotificationMixin, ListCreateAPIView):
    pass


class NotificationDetail(NotificationMixin, RetrieveUpdateDestroyAPIView):
    pass
