# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ping'
        db.create_table(u'pings_ping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('pub_status', self.gf('django.db.models.fields.CharField')(default='P', max_length=1)),
            ('pub_date', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pings', null=True, to=orm['days.Day'])),
            ('pub_time', self.gf('django.db.models.fields.TimeField')()),
            ('api_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'pings', ['Ping'])


    def backwards(self, orm):
        # Deleting model 'Ping'
        db.delete_table(u'pings_ping')


    models = {
        u'days.day': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Day'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pings.ping': {
            'Meta': {'object_name': 'Ping'},
            'api_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'pub_date': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pings'", 'null': 'True', 'to': u"orm['days.Day']"}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'}),
            'pub_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['pings']