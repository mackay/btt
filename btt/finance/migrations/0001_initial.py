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
        ('engagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommitmentAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('commitment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Commitment')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('engagement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engagement.Engagement')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='DonationPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Cause')),
            ],
        ),
        migrations.CreateModel(
            name='UserCause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affinity', models.FloatField(default=0.0)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Cause')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.DonationPool'),
        ),
        migrations.AddField(
            model_name='commitmentallocation',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.DonationPool'),
        ),
    ]
