# coding: utf-8
from django.test import TestCase
from datetime import datetime
from chuckchurros.core.models import Artigos

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