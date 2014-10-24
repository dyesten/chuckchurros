# coding: utf-8
from django.test import TestCase
from chuckchurros.core.models import Contatos
from chuckchurros.core.forms import ContatoForm

class ContatosTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/contato/')
	
	def test_get(self):
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'contato.html')
	
	def test_fields(self):
		form = ContatoForm()
		self.assertItemsEqual(['nome', 'email', 'telefone', 'comentario'], form.fields)
	
	def test_html(self):
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 5)
		self.assertContains(self.resp, 'type="text"', 2)
		self.assertContains(self.resp, 'type="email"')
		self.assertContains(self.resp, '<textarea ', 1)
		self.assertContains(self.resp, '<button ', 1)
	
	def test_csrf(self):
		self.assertContains(self.resp, 'csrfmiddlewaretoken')
	
	def test_context(self):
		form = self.resp.context['form']
		self.assertIsInstance(form, ContatoForm)

class ContatosPostTest(TestCase):
	def setUp(self):
		data = dict(nome='Dyesten Paulon', email='dyesten.pt@gmail.com', telefone='31-88996655', comentario='simples comentario')
		self.resp = self.client.post('/contato/', data)
		
	def test_post(self):
		self.assertEqual(302, self.resp.status_code)
	
	def test_save(self):
		self.assertTrue(Contatos.objects.exists())

class ContatoSucessoTest(TestCase):
	def setUp(self):
		s = Contatos.objects.create(nome='Dyesten Paulon', email='dyesten.pt@gmail.com', telefone='31-88996655', comentario='simples comentario')
		self.resp = self.client.get('/contato_sucesso/%d/' % s.pk)
	
	def test_get(self):
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'contato_sucesso.html')
	
	def test_not_found(self):
		response = self.client.get('/contato_sucesso/abc/')
		self.assertEqual(404, response.status_code)