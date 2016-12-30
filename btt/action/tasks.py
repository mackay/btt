from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def engage_negativity_direct():
    pass


@shared_task
def engage_negativity_followers():
    pass


@shared_task
def engage_positivity_direct():
    pass


@shared_task
def engage_positivity_followers():
    print "engage_positivity_followers task has executed"
