# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AcessoArtigo'
        #db.delete_table(u'core_acessoartigo')
        #db.delete_table('tb_ranking_artigos')

        # Adding model 'RankingArtigo'
        db.create_table('tb_ranking_artigos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idArtigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Artigos'])),
            ('ranking', self.gf('django.db.models.fields.IntegerField')()),
            ('ipUsuario', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('pcUsuario', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('dataRanking', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['RankingArtigo'])


    def backwards(self, orm):
        # Adding model 'AcessoArtigo'
        '''db.create_table(u'core_acessoartigo', (
            ('dataAcesso', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idArtigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Artigos'])),
        ))
        db.send_create_signal(u'core', ['AcessoArtigo'])
		'''

        # Deleting model 'RankingArtigo'
        db.delete_table('tb_ranking_artigos')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.artigos': {
            'Meta': {'object_name': 'Artigos', 'db_table': "'tb_artigos'"},
            'artigo': ('tinymce.models.HTMLField', [], {}),
            'dataAlteracao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dataCadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.contatos': {
            'Meta': {'object_name': 'Contatos', 'db_table': "'tb_contatos'"},
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'dataCadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        },
        u'core.rankingartigo': {
            'Meta': {'object_name': 'RankingArtigo', 'db_table': "'tb_ranking_artigos'"},
            'dataRanking': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idArtigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Artigos']"}),
            'ipUsuario': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'pcUsuario': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'ranking': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']