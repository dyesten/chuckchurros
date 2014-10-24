from django import forms
from chuckchurros.core.models import Contatos

class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contatos