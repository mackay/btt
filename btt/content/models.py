from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Cause(models.Model):
    name = models.CharField(max_length=255)


class Organization(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    contact_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    notes = models.TextField(default="")
    causes = models.ManyToManyField(Cause)


class EngagementContent(models.Model):
    created_by = models.ForeignKey(User)
    last_updated = models.DateTimeField(default=timezone.now)

    content = models.CharField(max_length=140)
    resource_url = models.CharField(max_length=255)
    cause = models.ForeignKey(Cause)