# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0001_initial'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_status', models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Draft'), (b'P', b'Published')])),
                ('headline', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100)),
                ('text', models.TextField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('lede_art', models.ForeignKey(to='photos.Photo')),
                ('pub_date', models.OneToOneField(related_name='post_for', to='days.Day')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
