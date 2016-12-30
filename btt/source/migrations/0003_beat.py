# -*- coding: utf-8 -*-
# Manually created by dpm on 2016-12-30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import dateutil.parser


def forwards_func(apps, schema_editor):
    Crontab = apps.get_model("django_celery_beat", "CrontabSchedule")
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")

    tab = Crontab( minute="0" )
    tab.save()
    task = PeriodicTask( name="collect-100-tweets",
                         task="source.tasks.collect_tweets",
                         crontab=tab,
                         args="[100]" )
    task.save()


    tab = Crontab( minute="30" )
    tab.save()
    task = PeriodicTask( name="classify-tweets",
                         task="source.tasks.classify_tweets",
                         crontab=tab,
                         args="[]" )
    task.save()



def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0001_initial'),
        ('source', '0002_data'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
