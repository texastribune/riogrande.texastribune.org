# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0001_initial'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField()),
                ('pub_status', models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Draft'), (b'P', b'Published')])),
                ('headline', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100)),
                ('author', models.CharField(default='', max_length=150)),
                ('author_email', models.EmailField(max_length=100)),
                ('summary', models.TextField()),
                ('text', models.TextField()),
                ('day_pub_date', models.OneToOneField(related_name='story_for', null=True, to='days.Day')),
                ('lede_art', models.ForeignKey(to='photos.Photo')),
            ],
            options={
                'verbose_name_plural': 'stories',
            },
            bases=(models.Model,),
        ),
    ]
