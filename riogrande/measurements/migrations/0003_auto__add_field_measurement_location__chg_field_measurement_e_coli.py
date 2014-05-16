# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Measurement.location'
        db.add_column(u'measurements_measurement', 'location',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(default='POINT(0.0 0.0)'),
                      keep_default=False)


        # Changing field 'Measurement.e_coli'
        db.alter_column(u'measurements_measurement', 'e_coli', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Measurement.location'
        db.delete_column(u'measurements_measurement', 'location')


        # Changing field 'Measurement.e_coli'
        db.alter_column(u'measurements_measurement', 'e_coli', self.gf('django.db.models.fields.FloatField')(null=True))

    models = {
        u'measurements.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'air_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'conductivity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dissolved_oxygen': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'e_coli': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT(0.0 0.0)'"}),
            'ph_level': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'secchi_disk_transparency': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'water_temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['measurements']