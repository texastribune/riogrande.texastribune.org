# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Day', fields ['date']
        db.create_unique(u'days_day', ['date'])


    def backwards(self, orm):
        # Removing unique constraint on 'Day', fields ['date']
        db.delete_unique(u'days_day', ['date'])


    models = {
        u'days.day': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Day'},
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['days']