# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.location'
        db.add_column(u'posts_post', 'location',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(default='POINT(-97 20)'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.location'
        db.delete_column(u'posts_post', 'location')


    models = {
        u'photos.photo': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lede_art': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photos.Photo']"}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['posts']