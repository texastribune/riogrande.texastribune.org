# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('pub_status', models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Draft'), (b'P', b'Published')])),
            ],
            options={
                'ordering': ['-pub_date__date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photos/%Y/%m')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('caption', models.TextField(blank=True)),
                ('credit', models.CharField(max_length=50, verbose_name=b'photographer', blank=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pub_status', models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Draft'), (b'P', b'Published')])),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gallery',
            name='photos',
            field=sortedm2m.fields.SortedManyToManyField(related_name='galleries', to='photos.Photo', blank=True, help_text=None, null=True, verbose_name=b'photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='pub_date',
            field=models.OneToOneField(related_name='gallery_for', null=True, to='days.Day'),
            preserve_default=True,
        ),
    ]
