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

    tab = Crontab( minute="0", hour="22" )
    tab.save()
    task = PeriodicTask( name="engage-negativity-directly-daily",
                         task="action.tasks.engage_negativity_direct",
                         crontab=tab,
                         args="[]" )
    task.save()

    tab = Crontab( minute="0", hour="23" )
    tab.save()
    task = PeriodicTask( name="engage-negativity-followers-daily",
                         task="action.tasks.engage_negativity_followers",
                         crontab=tab,
                         args="[]" )
    task.save()

    tab = Crontab( minute="0", hour="0" )
    tab.save()
    task = PeriodicTask( name="engage-positivity-directly-daily",
                         task="action.tasks.engage_positivity_direct",
                         crontab=tab,
                         args="[]" )
    task.save()

    tab = Crontab( minute="0", hour="1" )
    tab.save()
    task = PeriodicTask( name="engage-positivity-followers-daily",
                         task="action.tasks.engage_positivity_followers",
                         crontab=tab,
                         args="[]" )
    task.save()




def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0001_initial'),
        ('action', '0002_data'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
