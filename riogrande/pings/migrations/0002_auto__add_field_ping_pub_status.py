# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ping.pub_status'
        db.add_column(u'pings_ping', 'pub_status',
                      self.gf('django.db.models.fields.CharField')(default='P', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ping.pub_status'
        db.delete_column(u'pings_ping', 'pub_status')


    models = {
        u'pings.ping': {
            'Meta': {'object_name': 'Ping'},
            'api_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        }
    }

    complete_apps = ['pings']