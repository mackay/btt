# -*- coding: utf-8 -*-
# Manually created by dpm on 2016-12-29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

from django.contrib.auth import get_user_model


def forwards_func(apps, schema_editor):
    Cause = apps.get_model("content", "Cause")
    Response = apps.get_model("content", "Response")
    Organization = apps.get_model("content", "Organization")

    db_alias = schema_editor.connection.alias

    Cause.objects.using(db_alias).bulk_create([
        Cause(name="Women's Rights"),
        Cause(name="Racism"),
        Cause(name="Immigration"),
        Cause(name="Journalism"),
        Cause(name="LGBTQ Rights"),
        Cause(name="Environment"),
        Cause(name="Civility")
    ])

    User = get_user_model()
    creator = User.objects.create_superuser(username='btt', password='btt', email='')
    creator.save()

    # creator = User.objects.using(db_alias).all().first()

    cause_women = Cause.objects.using(db_alias).filter(name="Women's Rights").first()
    cause_journ = Cause.objects.using(db_alias).filter(name="Journalism").first()
    cause_civ = Cause.objects.using(db_alias).filter(name="Civility").first()

    Response.objects.using(db_alias).bulk_create([
        Response(content="This is an example tweet.", resource_url="google.com", created_by_id=creator.id, cause=cause_women),
        Response(content="A second tweet.", resource_url="google.com", created_by_id=creator.id, cause=cause_journ),
        Response(content="The final tweet.", resource_url="google.com", created_by_id=creator.id, cause=cause_civ)
    ])

    Organization.objects.using(db_alias).bulk_create([
        Organization( name="ACLU of Southern California",
                      url="https://www.aclusocal.org/",
                      rating=100.0,
                      contact_name="Hector Villagra",
                      contact_number="213.977.9500",
                      contact_email="fake@fake.com" )
    ])

    org = Organization( name="ACLU of Southern California",
                        url="https://www.aclusocal.org/",
                        rating=100.0,
                        contact_name="Hector Villagra",
                        contact_number="213.977.9500",
                        contact_email="fake@fake.com" )
    org.save()
    for cause in Cause.objects.all():
        org.causes.add( cause )


    org = Organization( name="Planned Parenthood Los Angeles",
                        url="https://www.plannedparenthood.org/planned-parenthood-los-angeles",
                        rating=100.0,
                        contact_name="Sue Dunlap",
                        contact_number="213-284-3200",
                        contact_email="fake@fake.com" )
    org.save()

    org.causes.add( Cause.objects.filter(name="Women's Rights").first() )


def reverse_func(apps, schema_editor):
    Cause = apps.get_model("content", "Cause")
    Response = apps.get_model("content", "Response")
    Organization = apps.get_model("content", "Organization")

    db_alias = schema_editor.connection.alias

    Cause.objects.using(db_alias).all().delete()
    Response.objects.using(db_alias).all().delete()
    Organization.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
