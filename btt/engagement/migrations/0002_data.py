# -*- coding: utf-8 -*-
# Manually created by dpm on 2016-12-29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
from django.db.models import Q
import django.db.models.deletion
import django.utils.timezone
import dateutil.parser




def forwards_func(apps, schema_editor):
    Campaign = apps.get_model("engagement", "Campaign")
    Engagement = apps.get_model("engagement", "Engagement")
    EngagementPurpose = apps.get_model("engagement", "EngagementPurpose")

    db_alias = schema_editor.connection.alias

    purposes = [
        EngagementPurpose(name="direct"),
        EngagementPurpose(name="followers"),
        EngagementPurpose(name="morale")
    ]
    for purpose in purposes:
        purpose.save()

    Cause = apps.get_model("content", "Cause")
    cause_civ = Cause.objects.filter(name="Civility").first()

    campaign = Campaign( name="",
                         start_date=dateutil.parser.parse('2016-12-01 02:00:00-08'),
                         end_date=dateutil.parser.parse('2017-01-31 20:00:00-08'),
                         interest=0.25,
                         audience=0.5,
                         sentiment=-0.25,
                         cause=cause_civ )
    campaign.save()

    EngagementContent = apps.get_model("content", "EngagementContent")
    engagement_content = EngagementContent.objects.filter(cause=cause_civ).first()

    Tweet = apps.get_model("classification", "Tweet")

    # sentiment filters will be <= if campaign sentiment is <0, >= if >0
    # interest and audience filters will be >= if campaign sentiment is >0
    # any filter will not be applied if the campaign value is 0 - this signifies it isn't important to the campaign

    civility_filter = Q(classification__classificationcause__cause=campaign.cause)
    sentiment_filter = Q(classification__sentiment__lte=campaign.sentiment)  # because campaign sentiment is < 0
    interest_filter = Q(classification__interest__gte=campaign.interest)  # because interest is > 0 (will always be >0)
    audience_filter = Q(classification__audience__gte=campaign.audience)  # because campaign audience is > 0 (will always be >0)

    tweet = Tweet.objects.filter( civility_filter, sentiment_filter, interest_filter, audience_filter).first()

    created_date = dateutil.parser.parse('2016-12-28 02:00:00-08')
    scheduled_date = dateutil.parser.parse('2017-01-3 14:00:00-08')
    engagement = Engagement( created_date=created_date,
                             scheduled_date=scheduled_date,
                             campaign=campaign,
                             content=engagement_content,
                             purpose=purposes[0],
                             tweet=tweet)
    engagement.save()



def reverse_func(apps, schema_editor):
    Campaign = apps.get_model("engagement", "Campaign")
    Engagement = apps.get_model("engagement", "Engagement")
    EngagementPurpose = apps.get_model("engagement", "EngagementPurpose")

    db_alias = schema_editor.connection.alias

    Campaign.objects.using(db_alias).all().delete()
    Engagement.objects.using(db_alias).all().delete()
    EngagementPurpose.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('engagement', '0001_initial'),
        ('content', '0002_data'),
        ('classification', '0002_data'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
