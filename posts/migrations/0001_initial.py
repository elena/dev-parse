# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'posts_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'posts', ['Author'])

        # Adding model 'Ticket'
        db.create_table(u'posts_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'posts', ['Ticket'])

        # Adding model 'Post'
        db.create_table(u'posts_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('author_original', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['posts.Author'])),
            ('posted_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('contents', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('views', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('last_checked_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'posts', ['Post'])

        # Adding M2M table for field tickets on 'Post'
        m2m_table_name = db.shorten_name(u'posts_post_tickets')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'posts.post'], null=False)),
            ('ticket', models.ForeignKey(orm[u'posts.ticket'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'ticket_id'])

        # Adding model 'PostChild'
        db.create_table(u'posts_postchild', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('author_original', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['posts.Author'])),
            ('posted_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('contents', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['posts.Post'])),
        ))
        db.send_create_signal(u'posts', ['PostChild'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'posts_author')

        # Deleting model 'Ticket'
        db.delete_table(u'posts_ticket')

        # Deleting model 'Post'
        db.delete_table(u'posts_post')

        # Removing M2M table for field tickets on 'Post'
        db.delete_table(db.shorten_name(u'posts_post_tickets'))

        # Deleting model 'PostChild'
        db.delete_table(u'posts_postchild')


    models = {
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
            'posted_at': ('django.db.models.fields.DateTimeField', [], {}),
            'tickets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['posts.Ticket']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'posts.postchild': {
            'Meta': {'object_name': 'PostChild'},
            'author_original': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['posts.Author']"}),
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['posts.Post']"}),
            'posted_at': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'posts.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['posts']