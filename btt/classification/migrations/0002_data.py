# -*- coding: utf-8 -*-
# Manually created by dpm on 2016-12-29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import dateutil.parser


def forwards_func(apps, schema_editor):
    TwitterAccount = apps.get_model("classification", "TwitterAccount")
    Tweet = apps.get_model("classification", "Tweet")
    Classification = apps.get_model("classification", "Classification")
    ClassificationCause = apps.get_model("classification", "ClassificationCause")
    # ClassificationMeta = apps.get_model("classification", "ClassificationMeta")

    db_alias = schema_editor.connection.alias

    trump = TwitterAccount( username="realDonaldTrump", name="", followers=18151875, following=41 )
    martin = TwitterAccount( username="MartinShkreli", name="Martin ShkreliVerified account", followers=189268, following=1217 )

    trump.save()
    martin.save()

    tweets = [
        Tweet( date=dateutil.parser.parse('2016-12-26 19:06:58-08'),
               url="https://twitter.com/realDonaldTrump/status/813578484572450816",
               likes=66440,
               retweets=16705,
               content="I gave millions of dollars to DJT Foundation, raised or recieved millions more, ALL of which is given to charity, and media won't report!",
               hashtags="",
               resource_url="",
               account=trump ),
        Tweet( date=dateutil.parser.parse('2016-12-07 16:41:58-08'),
               url="https://twitter.com/realDonaldTrump/status/806660011904614408",
               likes=50197,
               retweets=12924,
               content="Chuck Jones, who is President of United Steelworkers 1999, has done a terrible job representing workers. No wonder companies flee country!",
               hashtags="",
               resource_url="",
               account=trump ),
        Tweet( date=dateutil.parser.parse('2016-12-24 20:18:05-08'),
               url="https://twitter.com/MartinShkreli/status/812693883931004928",
               likes=283,
               retweets=28,
               content=". @laurenduca can we date?",
               hashtags="@laurenduca",
               resource_url="",
               account=martin ),
        Tweet( date=dateutil.parser.parse('2016-12-23 16:47:05-08'),
               url="https://twitter.com/MartinShkreli/status/812278389256179712",
               likes=117,
               retweets=16,
               content="Never mind the ceasefire. Back to full on war against Bloomberg @business",
               hashtags="@business",
               resource_url="",
               account=martin )
    ]
    for tweet in tweets:
        tweet.save()

    classifications = [
        Classification( classifier='fake',
                        interest=0.8,
                        audience=1.0,
                        sentiment=0.0,
                        tweet=tweets[0] ),
        Classification( classifier='fake',
                        interest=0.6,
                        audience=1.0,
                        sentiment=-0.8,
                        tweet=tweets[1] ),
        Classification( classifier='fake',
                        interest=0.2,
                        audience=0.2,
                        sentiment=0.0,
                        tweet=tweets[2] ),
        Classification( classifier='fake',
                        interest=0.6,
                        audience=0.2,
                        sentiment=-0.3,
                        tweet=tweets[3] )
    ]
    for classification in classifications:
        classification.save()

    Cause = apps.get_model("content", "Cause")
    cause_women = Cause.objects.filter(name="Women's Rights").first()
    cause_journ = Cause.objects.filter(name="Journalism").first()
    cause_civ = Cause.objects.filter(name="Civility").first()

    ClassificationCause.objects.using(db_alias).bulk_create([
        ClassificationCause( affinity=0.7, cause=cause_journ, classification=classifications[0]),
        ClassificationCause( affinity=0.6, cause=cause_civ, classification=classifications[1]),
        ClassificationCause( affinity=0.3, cause=cause_women, classification=classifications[2]),
        ClassificationCause( affinity=0.0, cause=cause_civ, classification=classifications[2]),
        ClassificationCause( affinity=0.5, cause=cause_journ, classification=classifications[3]),
    ])


def reverse_func(apps, schema_editor):
    TwitterAccount = apps.get_model("classification", "TwitterAccount")
    Tweet = apps.get_model("classification", "Tweet")
    Classification = apps.get_model("classification", "Classification")
    ClassificationCause = apps.get_model("classification", "ClassificationCause")
    ClassificationMeta = apps.get_model("classification", "ClassificationMeta")

    db_alias = schema_editor.connection.alias

    TwitterAccount.objects.using(db_alias).all().delete()
    Tweet.objects.using(db_alias).all().delete()
    Classification.objects.using(db_alias).all().delete()
    ClassificationCause.objects.using(db_alias).all().delete()
    ClassificationMeta.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0001_initial'),
        ('content', '0002_data'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
