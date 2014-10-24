# coding: utf-8
from django.test import TestCase
#from django.db import IntegrityError
from datetime import datetime
from django.core.exceptions import ValidationError
from chuckchurros.core.models import Artigos, AcessoArtigo, RankingArtigo, Contatos

class ArtigosTest(TestCase):
	def setUp(self):
		self.obj = Artigos(
			titulo='teste artigo um', 
			slug = 'teste-artigo-um', 
			artigo='texto qualquer para o artigo...',
			user_id=1
		)
	
	def test_create(self):
		self.obj.save()
		self.assertEqual(1, self.obj.pk)
	
	def test_has_created_at(self):
		self.obj.save()
		self.assertIsInstance(self.obj.dataCadastro, datetime)
		
	def test_unicode(self):
		self.assertEqual(u'teste artigo um',  unicode(self.obj))


class AcessoArtigoTest(TestCase):
	def setUp(self):
		self.obj = AcessoArtigo(
			artigos_id=1, 
			ipUsuario = '127.0.0.1', 
			pcUsuario='teste-pc'
		)
	
	def test_create(self):
		self.obj.save()
		self.assertEqual(1, self.obj.pk)
	
	def test_has_created_at(self):
		self.obj.save()
		self.assertIsInstance(self.obj.dataAcesso, datetime)
	


class RankingArtigoTest(TestCase):
	def setUp(self):
		self.obj = RankingArtigo(
			idArtigo_id=1, 
			ranking=5,
			ipUsuario = '127.0.0.1', 
			pcUsuario='teste-pc'
		)
	
	def test_create(self):
		self.obj.save()
		self.assertEqual(1, self.obj.pk)
	
	def test_has_created_at(self):
		self.obj.save()
		self.assertIsInstance(self.obj.dataRanking, datetime)
		

class ContatosTest(TestCase):
	def setUp(self):
		self.obj = Contatos(
			nome='Dyesten', 
			email='dyesten.pt@gmail.com',
			telefone = '(31)8748-2098', 
			comentario='acomentiosssdasdsdc fesda'
		)
	
	def test_create(self):
		self.obj.save()
		self.assertEqual(1, self.obj.pk)
	
	def test_has_created_at(self):
		self.obj.save()
		self.assertIsInstance(self.obj.dataCadastro, datetime)
		
	def test_unicode(self):
		self.assertEqual(u'Dyesten',  unicode(self.obj))