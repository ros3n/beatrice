from django.contrib.auth.models import User
from django.contrib.gis.db import models


TASK_STATUSES = (
    (0, 'inactive'),
    (1, 'active')
)

class Category(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)


class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    status = models.IntegerField(choices=TASK_STATUSES, default=1)
    # point = models.PointField(help_text=u'(longitude/latitude)')
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    radius = models.IntegerField()
    category = models.ForeignKey(Category, related_name='tasks')
    user = models.ForeignKey(User, related_name='tasks')


class Notification(models.Model):
    date = models.DateTimeField()
    task = models.ForeignKey(Task, related_name='notifications')
