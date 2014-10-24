# coding: utf-8
from django.test import TestCase

class SobreTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/sobre/')
	
	def test_get(self):
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'sobre.html')