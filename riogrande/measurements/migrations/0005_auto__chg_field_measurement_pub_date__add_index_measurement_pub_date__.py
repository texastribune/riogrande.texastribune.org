# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Measurement.pub_date' to match new field type.
        db.rename_column(u'measurements_measurement', 'pub_date', 'pub_date_id')
        # Changing field 'Measurement.pub_date'
        db.alter_column(u'measurements_measurement', 'pub_date_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['days.Day']))
        # Adding index on 'Measurement', fields ['pub_date']
        db.create_index(u'measurements_measurement', ['pub_date_id'])

        # Adding unique constraint on 'Measurement', fields ['pub_date']
        db.create_unique(u'measurements_measurement', ['pub_date_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Measurement', fields ['pub_date']
        db.delete_unique(u'measurements_measurement', ['pub_date_id'])

        # Removing index on 'Measurement', fields ['pub_date']
        db.delete_index(u'measurements_measurement', ['pub_date_id'])


        # Renaming column for 'Measurement.pub_date' to match new field type.
        db.rename_column(u'measurements_measurement', 'pub_date_id', 'pub_date')
        # Changing field 'Measurement.pub_date'
        db.alter_column(u'measurements_measurement', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 15, 0, 0)))

    models = {
        u'days.day': {
            'Meta': {'object_name': 'Day'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'measurements.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'air_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'conductivity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dissolved_oxygen': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'e_coli': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'ph_level': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'measurement_for'", 'unique': 'True', 'null': 'True', 'to': u"orm['days.Day']"}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'secchi_disk_transparency': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'water_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['measurements']