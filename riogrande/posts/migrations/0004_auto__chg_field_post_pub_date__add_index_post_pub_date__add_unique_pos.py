# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Post.pub_date' to match new field type.
        db.rename_column(u'posts_post', 'pub_date', 'pub_date_id')
        # Changing field 'Post.pub_date'
        db.alter_column(u'posts_post', 'pub_date_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['days.Day']))
        # Adding index on 'Post', fields ['pub_date']
        db.create_index(u'posts_post', ['pub_date_id'])

        # Adding unique constraint on 'Post', fields ['pub_date']
        db.create_unique(u'posts_post', ['pub_date_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Post', fields ['pub_date']
        db.delete_unique(u'posts_post', ['pub_date_id'])

        # Removing index on 'Post', fields ['pub_date']
        db.delete_index(u'posts_post', ['pub_date_id'])


        # Renaming column for 'Post.pub_date' to match new field type.
        db.rename_column(u'posts_post', 'pub_date_id', 'pub_date')
        # Changing field 'Post.pub_date'
        db.alter_column(u'posts_post', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'days.day': {
            'Meta': {'object_name': 'Day'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
            'pub_date': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'post_for'", 'unique': 'True', 'to': u"orm['days.Day']"}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['posts']