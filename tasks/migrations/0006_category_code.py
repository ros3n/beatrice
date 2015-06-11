# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150514_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='code',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
