# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='latitude',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='longitude',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=8),
            preserve_default=False,
        ),
    ]
