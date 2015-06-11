# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_category_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=8, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=8, blank=True),
        ),
    ]
