from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class TwitterAccount(models.Model):
    username = models.CharField(max_length=16)
    name = models.CharField(max_length=255)

    last_updated = models.DateTimeField(default=timezone.now)
    last_engaged = models.DateTimeField(default=None, null=True)

    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)


class Tweet(models.Model):
    account = models.ForeignKey(TwitterAccount)
    date = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)

    content = models.CharField(max_length=140)

    hashtags = models.CharField(max_length=255)
    resource_url = models.CharField(max_length=255)

    last_updated = models.DateTimeField(default=timezone.now)
    last_engaged = models.DateTimeField(default=None, null=True)


class Classification(models.Model):
    tweet = models.ForeignKey(Tweet)
    classifier = models.CharField(max_length=255)

    interest = models.FloatField(default=0.0)
    audience = models.FloatField(default=0.0)
    sentiment = models.FloatField(default=0.0)

    last_updated = models.DateTimeField(default=timezone.now)


class ClassificationCause(models.Model):
    classification = models.ForeignKey(Classification)
    cause = models.ForeignKey('content.Cause')
    affinity = models.FloatField(default=0.0)


class ClassificationMeta(models.Model):
    classification = models.ForeignKey(Classification)
    key = models.CharField(max_length=64)
    text = models.TextField(default="")
    numeric = models.FloatField(default=0.0)
