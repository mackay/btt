from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def collect_tweets(maximum_count=None):
    print "collect_tweets task has executed"


@shared_task
def classify_tweets():
    pass
