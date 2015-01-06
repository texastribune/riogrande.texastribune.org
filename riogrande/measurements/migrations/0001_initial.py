# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_status', models.CharField(default=b'D', max_length=1, choices=[(b'D', b'Draft'), (b'P', b'Published')])),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('air_temperature', models.FloatField(help_text='in degrees Celsius', null=True, blank=True)),
                ('conductivity', models.FloatField(help_text='in \u03bcS/cm', null=True, blank=True)),
                ('depth', models.FloatField(help_text='in meters', null=True, blank=True)),
                ('dissolved_oxygen', models.FloatField(help_text='in mg/L', null=True, blank=True)),
                ('e_coli', models.IntegerField(help_text='colonies per 100 ml', null=True, blank=True)),
                ('ph_level', models.FloatField(blank=True, help_text='must be between 0.0 and 14.0', null=True, validators=[django.core.validators.MaxValueValidator(14.0), django.core.validators.MinValueValidator(0.0)])),
                ('secchi_disk_transparency', models.FloatField(help_text='in meters', null=True, blank=True)),
                ('water_temperature', models.FloatField(help_text='in degrees Celsius', null=True, blank=True)),
                ('pub_date', models.OneToOneField(related_name='measurement_for', null=True, to='days.Day')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
