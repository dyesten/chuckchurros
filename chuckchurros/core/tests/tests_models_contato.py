# coding: utf-8
from django.test import TestCase
from datetime import datetime
from chuckchurros.core.models import Contatos

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