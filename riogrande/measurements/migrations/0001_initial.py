# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Measurement'
        db.create_table(u'measurements_measurement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.related.OneToOneField')(related_name='measurement_for', unique=True, null=True, to=orm['days.Day'])),
            ('pub_status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('air_temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('conductivity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('depth', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dissolved_oxygen', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('e_coli', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ph_level', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('secchi_disk_transparency', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('water_temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'measurements', ['Measurement'])


    def backwards(self, orm):
        # Deleting model 'Measurement'
        db.delete_table(u'measurements_measurement')


    models = {
        u'days.day': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Day'},
            'date': ('django.db.models.fields.DateField', [], {}),
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