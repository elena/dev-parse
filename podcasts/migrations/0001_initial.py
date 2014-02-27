# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Podcast'
        db.create_table(u'podcasts_podcast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'podcasts', ['Podcast'])

        # Adding model 'PostPodcast'
        db.create_table(u'podcasts_postpodcast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('podcast', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['podcasts.Podcast'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['posts.Post'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'podcasts', ['PostPodcast'])


    def backwards(self, orm):
        # Deleting model 'Podcast'
        db.delete_table(u'podcasts_podcast')

        # Deleting model 'PostPodcast'
        db.delete_table(u'podcasts_postpodcast')


    models = {
        u'podcasts.podcast': {
            'Meta': {'object_name': 'Podcast'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'podcasts.postpodcast': {
            'Meta': {'object_name': 'PostPodcast'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'podcast': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['podcasts.Podcast']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['posts.Post']"})
        },
        u'posts.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'author_original': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['posts.Author']"}),
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checked_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'num_posts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'num_views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'posted_at': ('django.db.models.fields.DateTimeField', [], {}),
            'tickets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['posts.Ticket']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'posts.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['podcasts']