# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'photos_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('pub_status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
        ))
        db.send_create_signal(u'photos', ['Photo'])

        # Adding model 'Gallery'
        db.create_table(u'photos_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.related.OneToOneField')(related_name='gallery_for', unique=True, null=True, to=orm['days.Day'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pub_status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
        ))
        db.send_create_signal(u'photos', ['Gallery'])


        # Adding SortedM2M table for field photos on 'Gallery'
        db.create_table(u'photos_gallery_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm[u'photos.gallery'], null=False)),
            ('photo', models.ForeignKey(orm[u'photos.photo'], null=False)),
            ('sort_value', models.IntegerField())
        ))
        db.create_unique(u'photos_gallery_photos', ['gallery_id', 'photo_id'])

    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'photos_photo')

        # Deleting model 'Gallery'
        db.delete_table(u'photos_gallery')

        # Removing M2M table for field photos on 'Gallery'
        db.delete_table(db.shorten_name(u'photos_gallery_photos'))


    models = {
        u'days.day': {
            'Meta': {'object_name': 'Day'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'photos.gallery': {
            'Meta': {'ordering': "['-pub_date__date']", 'object_name': 'Gallery'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos': ('sortedm2m.fields.SortedManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['photos.Photo']"}),
            'pub_date': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'gallery_for'", 'unique': 'True', 'null': 'True', 'to': u"orm['days.Day']"}),
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