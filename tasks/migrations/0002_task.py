# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('status', models.IntegerField(default=1, choices=[(0, b'inactive'), (1, b'active')])),
                ('radius', models.IntegerField()),
                ('category', models.ForeignKey(related_name='tasks', to='tasks.Category')),
            ],
        ),
    ]
