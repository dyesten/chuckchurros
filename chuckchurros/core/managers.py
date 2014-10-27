# coding: latin
from django.db import models
from datetime import time
from django.db.models import Count

class ArtigosManager(models.Manager):
	def qtdVisualizacao(self):
		qs = self.select_related('AcessoArtigo').annotate(qtd_visualizacao=Count('artigos_id'))
		return qs
	
	def top5Recentes(self):
		qs = self.objects.order_by('-dataCadastro')[:5]
		return qs#.all()
	
	def top5Acessadas(self):
		qs = self.select_related('AcessoArtigo').annotate(Count('artigos_id')).order_by('-artigos_id__count')[:5]
		return qs
		

class EquipeManager(models.Manager):
	def membros(self):
		qs = self.all().order_by('dataCadastro')		
		return qs