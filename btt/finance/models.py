from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserCause(models.Model):
    user = models.ForeignKey(User)
    cause = models.ForeignKey('content.models.Cause')
    affinity = models.FloatField(default=0.0)
    last_updated = models.DateTimeField(default=timezone.now)


class Commitment(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)


class DonationPool(models.Model):
    cause = models.ForeignKey('content.models.Cause')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=11, decimal_places=2)


class CommitmentAllocation(models.Model):
    commitment = models.ForeignKey(Commitment)
    pool = models.ForeignKey(DonationPool)

    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)


class Donation(models.Model):
    organization = models.ForeignKey('content.models.Organization')
    engagement = models.ForeignKey('engagement.models.Engagement')
    pool = models.ForeignKey(DonationPool)

    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
