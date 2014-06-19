# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Story'
        db.create_table(u'stories_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('day_pub_date', self.gf('django.db.models.fields.related.OneToOneField')(related_name='story_for', unique=True, null=True, to=orm['days.Day'])),
            ('pub_status', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.CharField')(default=u'', max_length=150)),
            ('author_email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('lede_art', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'])),
        ))
        db.send_create_signal(u'stories', ['Story'])


    def backwards(self, orm):
        # Deleting model 'Story'
        db.delete_table(u'stories_story')


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
        u'stories.story': {
            'Meta': {'object_name': 'Story'},
            'author': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '150'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'day_pub_date': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'story_for'", 'unique': 'True', 'null': 'True', 'to': u"orm['days.Day']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lede_art': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photos.Photo']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'pub_status': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['stories']