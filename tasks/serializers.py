from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from tasks.models import Category, Task, Notification


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'name', 'description', 'status', 'point', 'radius',
            'category',
        )
        read_only_fields = ('notifications',)


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('date', 'task')
