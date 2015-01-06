# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('pub_status', models.CharField(default=b'P', max_length=1, choices=[(b'D', b'Draft'), (b'P', b'Published')])),
                ('pub_time', models.TimeField()),
                ('api_id', models.PositiveIntegerField(unique=True)),
                ('pub_date', models.ForeignKey(related_name='pings', to='days.Day', null=True)),
            ],
            options={
                'ordering': ('api_id',),
            },
            bases=(models.Model,),
        ),
    ]
