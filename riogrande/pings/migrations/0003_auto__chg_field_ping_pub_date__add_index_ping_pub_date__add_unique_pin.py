# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ping.pub_time'
        db.add_column(u'pings_ping', 'pub_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 0)),
                      keep_default=False)


        # Renaming column for 'Ping.pub_date' to match new field type.
        db.rename_column(u'pings_ping', 'pub_date', 'pub_date_id')
        # Changing field 'Ping.pub_date'
        db.alter_column(u'pings_ping', 'pub_date_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['days.Day']))
        # Adding index on 'Ping', fields ['pub_date']
        db.create_index(u'pings_ping', ['pub_date_id'])


    def backwards(self, orm):
        # Removing index on 'Ping', fields ['pub_date']
        db.delete_index(u'pings_ping', ['pub_date_id'])

        # Deleting field 'Ping.pub_time'
        db.delete_column(u'pings_ping', 'pub_time')


        # Renaming column for 'Ping.pub_date' to match new field type.
        db.rename_column(u'pings_ping', 'pub_date_id', 'pub_date')
        # Changing field 'Ping.pub_date'
        db.alter_column(u'pings_ping', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 16, 0, 0)))

    models = {
        u'days.day': {
            'Meta': {'object_name': 'Day'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pings.ping': {
            'Meta': {'object_name': 'Ping'},
            'api_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'pub_date': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ping_for'", 'null': 'True', 'to': u"orm['days.Day']"}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'}),
            'pub_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['pings']