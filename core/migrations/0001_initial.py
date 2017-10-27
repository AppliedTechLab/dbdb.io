# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 20:21
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64)),
                ('multivalued', models.NullBooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeatureOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=64)),
                ('feature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Feature')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('website', models.URLField(default=None, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('website', models.URLField(default='', null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('website', models.URLField(default='', null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('authors', models.CharField(blank=True, max_length=255)),
                ('bibtex', models.TextField(blank=True, default=None, null=True)),
                ('link', models.URLField(blank=True, default=None, null=True)),
                ('year', models.IntegerField(default=0, null=True)),
                ('number', models.IntegerField(default=1, null=True)),
                ('cite', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuggestedSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('approved', models.NullBooleanField()),
                ('secret_key', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('current_version', models.PositiveIntegerField(default=1)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('secret_key', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.PositiveIntegerField(default=1)),
                ('is_current', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('version_message', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, default='')),
                ('history', models.TextField(blank=True, default='')),
                ('website', models.URLField(blank=True, default='', null=True)),
                ('tech_docs', models.URLField(blank=True, default='', null=True)),
                ('developer', models.CharField(blank=True, default='', max_length=512)),
                ('start_year', models.CharField(blank=True, default='', max_length=128)),
                ('end_year', models.CharField(blank=True, default='', max_length=128)),
                ('logo_orig', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='logos')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_type', models.ManyToManyField(blank=True, to='core.ProjectType')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.System')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemVersionMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('derived_from', models.ManyToManyField(blank=True, related_name='systems_derived', to='core.System')),
                ('licenses', models.ManyToManyField(blank=True, related_name='systems_licenses', to='core.License')),
                ('oses', models.ManyToManyField(blank=True, related_name='systems_oses', to='core.OperatingSystem')),
                ('publications', models.ManyToManyField(blank=True, related_name='systems_publications', to='core.Publication')),
                ('supported_languages', models.ManyToManyField(blank=True, related_name='systems_supported', to='core.ProgrammingLanguage')),
                ('written_in', models.ManyToManyField(blank=True, related_name='systems_written', to='core.ProgrammingLanguage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]