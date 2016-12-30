# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 07:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.CharField(max_length=140)),
                ('resource_url', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0)),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255)),
                ('contact_email', models.CharField(max_length=255)),
                ('notes', models.TextField(default='')),
                ('causes', models.ManyToManyField(to='content.Cause')),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='cause',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Cause'),
        ),
    ]
