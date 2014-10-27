from django.conf.urls import patterns, include, url
from chuckchurros.core.views import ContatoSucesso, ContatoCreate

urlpatterns = patterns('chuckchurros.core.views',
    url(r'^$', 'home', name='home'),
	url(r'^sobre/$', 'sobre', name='sobre'),
	url(r'^contato/$', ContatoCreate.as_view(), name='contato'),
	url(r'^artigosRecentes/$', 'artigosRecentes', name='artigosRecentes'),
	url(r'^artigosMaisAcessados/$', 'artigosMaisAcessados', name='artigosMaisAcessados'),
	url(r'^artigosMaisVotados/$', 'artigosMaisVotados', name='artigosMaisVotados'),
	url(r'^classifica_artigo/(\d+)/(\d+)/$', 'classifica_artigo', name='classifica_artigo'),
	url(r'^contato_sucesso/(?P<pk>\d+)/$', ContatoSucesso.as_view(), name='contato_sucesso'),
	url(r'^artigo/(?P<slug>[a-zA-Z0-9-_\.]+)/$', 'artigo', name='artigo'),
)