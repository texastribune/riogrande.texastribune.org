# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Photo.date_added'
        db.delete_column(u'photos_photo', 'date_added')

        # Deleting field 'Photo.is_public'
        db.delete_column(u'photos_photo', 'is_public')

        # Adding field 'Photo.pub_date'
        db.add_column(u'photos_photo', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Photo.pub_status'
        db.add_column(u'photos_photo', 'pub_status',
                      self.gf('django.db.models.fields.CharField')(default='D', max_length=1),
                      keep_default=False)

        # Deleting field 'Gallery.is_public'
        db.delete_column(u'photos_gallery', 'is_public')

        # Deleting field 'Gallery.date_added'
        db.delete_column(u'photos_gallery', 'date_added')

        # Adding field 'Gallery.pub_date'
        db.add_column(u'photos_gallery', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Gallery.pub_status'
        db.add_column(u'photos_gallery', 'pub_status',
                      self.gf('django.db.models.fields.CharField')(default='D', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Photo.date_added'
        db.add_column(u'photos_photo', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Photo.is_public'
        db.add_column(u'photos_photo', 'is_public',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'Photo.pub_date'
        db.delete_column(u'photos_photo', 'pub_date')

        # Deleting field 'Photo.pub_status'
        db.delete_column(u'photos_photo', 'pub_status')

        # Adding field 'Gallery.is_public'
        db.add_column(u'photos_gallery', 'is_public',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Gallery.date_added'
        db.add_column(u'photos_gallery', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'Gallery.pub_date'
        db.delete_column(u'photos_gallery', 'pub_date')

        # Deleting field 'Gallery.pub_status'
        db.delete_column(u'photos_gallery', 'pub_status')


    models = {
        u'photos.gallery': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Gallery'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos': ('sortedm2m.fields.SortedManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['photos.Photo']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        }
    }

    complete_apps = ['photos']