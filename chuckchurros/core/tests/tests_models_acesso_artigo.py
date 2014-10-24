# coding: utf-8
from django.test import TestCase
from datetime import datetime
from chuckchurros.core.models import AcessoArtigo

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