from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )
from tasks.models import Task, Category, Notification
from tasks.serializers import TaskSerializer

class TaskMixin(object):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskList(TaskMixin, ListCreateAPIView):
    pass


class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
    pass
