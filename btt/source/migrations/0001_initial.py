# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classifier', models.CharField(max_length=255)),
                ('interest', models.FloatField(default=0.0)),
                ('audience', models.FloatField(default=0.0)),
                ('sentiment', models.FloatField(default=0.0)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ClassificationCause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affinity', models.FloatField(default=0.0)),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Cause')),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Classification')),
            ],
        ),
        migrations.CreateModel(
            name='ClassificationMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('text', models.TextField(default='')),
                ('numeric', models.FloatField(default=0.0)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Classification')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.CharField(max_length=255)),
                ('likes', models.IntegerField(default=0)),
                ('retweets', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=140)),
                ('hashtags', models.CharField(max_length=255)),
                ('resource_url', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_engaged', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_engaged', models.DateTimeField(default=None, null=True)),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Account'),
        ),
        migrations.AddField(
            model_name='classification',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Tweet'),
        ),
    ]