# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

from cloudinary.models import CloudinaryField
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^cloudinary\.models\.CloudinaryField"])

from chuckchurros.core.managers import ArtigosManager, EquipeManager


class Artigos(models.Model):
	titulo = models.CharField(max_length=250)
	slug = models.SlugField(_('Slug'), null=False, blank=False)
	artigo = HTMLField()
	user = models.ForeignKey(User)
	dataCadastro = models.DateTimeField(auto_now_add=True)
	dataAlteracao = models.DateTimeField(auto_now=True)
	objects = ArtigosManager()
	
	def __unicode__(self):
		return self.titulo
	
	class Meta:
		db_table = "tb_artigos"
		ordering = ['-dataCadastro']
		verbose_name = _('Artigo')
		verbose_name_plural = _('Artigos')


class AcessoArtigo(models.Model):
	artigos = models.ForeignKey('Artigos', related_name="artigos_id")
	ipUsuario = models.CharField(max_length=200, null=True, blank=False)
	pcUsuario = models.CharField(max_length=200, null=True, blank=False)
	dataAcesso = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		db_table = "tb_acesso_artigos"
		

class RankingArtigo(models.Model):
	idArtigo = models.ForeignKey('Artigos', related_name="id_artigo")
	ranking = models.IntegerField(null=False)
	ipUsuario = models.CharField(max_length=200, null=True, blank=False)
	pcUsuario = models.CharField(max_length=200, null=True, blank=False)
	dataRanking = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		db_table = "tb_ranking_artigos"


class Contatos(models.Model):
	nome = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	telefone = models.CharField(max_length=15, null=True)
	comentario = models.TextField()
	dataCadastro = models.DateTimeField(auto_now_add=True)	
	
	def __unicode__(self):
		return self.nome		
	
	@models.permalink
	def get_absolute_url(self):
		return ('core:contato_sucesso', (), {'pk':self.pk})
		
	class Meta:
		db_table = "tb_contatos"
		verbose_name = _('contato')
		verbose_name_plural = _('contatos')
	


class Equipe(models.Model):
	foto = CloudinaryField('foto', null=True, blank=True)
	nome = models.CharField(max_length=100, null=False, blank=False)
	descricao = models.TextField()
	dataCadastro = models.DateTimeField(auto_now_add=True)
	
	objects = EquipeManager()
	
	def __unicode__(self):
		return self.nome
	
	class Meta:
		verbose_name = _('membro')
		verbose_name_plural = _('membros')