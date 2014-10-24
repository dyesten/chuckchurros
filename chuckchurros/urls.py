from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('chuckchurros.core.views',
    url(r'^$', 'home', name='home'),
	url(r'^sobre/$', 'sobre', name='sobre'),
	url(r'^contato/$', 'contato', name='contato'),
	url(r'^artigosRecentes/$', 'artigosRecentes', name='artigosRecentes'),
	url(r'^artigosMaisAcessados/$', 'artigosMaisAcessados', name='artigosMaisAcessados'),
	url(r'^artigosMaisVotados/$', 'artigosMaisVotados', name='artigosMaisVotados'),
	url(r'^classifica_artigo/(\d+)/(\d+)/$', 'classifica_artigo', name='classifica_artigo'),
	url(r'^contato_sucesso/(\d+)/$', 'contato_sucesso', name='contato_sucesso'),
	url(r'^artigo/(?P<slug>[a-zA-Z0-9-_\.]+)/$', 'artigo', name='artigo'),
    url(r'^admin/', include(admin.site.urls)),
	(r'^tinymce/', include('tinymce.urls')),
)