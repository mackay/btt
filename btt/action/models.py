from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    cause = models.ForeignKey('content.Cause')

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()

    interest = models.FloatField(default=0.0)
    audience = models.FloatField(default=0.0)
    sentiment = models.FloatField(default=0.0)


class EngagementPurpose(models.Model):
    name = models.CharField(max_length=255)


class Engagement(models.Model):
    campaign = models.ForeignKey(Campaign)
    response = models.ForeignKey('content.Response')
    tweet = models.ForeignKey('source.Tweet')

    purpose = models.ForeignKey(EngagementPurpose, null=True, default=None)

    created_date = models.DateTimeField(default=timezone.now)
    scheduled_date = models.DateTimeField(default=None, null=True)
    action_date = models.DateTimeField(default=None, null=True)
