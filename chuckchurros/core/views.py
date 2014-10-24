# coding: utf-8
from django.core.mail import send_mail
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from chuckchurros.core.forms import ContatoForm
from chuckchurros.core.models import Artigos, Contatos, RankingArtigo, AcessoArtigo
from django.db.models import Avg, Sum
from django.db.models import Count
from django.db import connection
import json



def enviarEmailComentario(obj):	
	titulo = 'Novo mensagem recebida pelo site'
	destino = 'dyesten.pt@gmail.com'
	texto = "\nNome: "+(obj.nome)+" \nE-mail: "+(obj.email)+" \nMensagem: "+(obj.comentario)
	
	send_mail(subject=titulo, message=texto, from_email=destino, recipient_list=[destino],	)


def home(request):
	'''context = { "artigos":Artigos.objects.raw('select a.id, a.titulo, a.slug, a.artigo, a.dataCadastro, a.dataAlteracao, ac.qtd_visualizacao from tb_artigos a '+
												'left join (select artigos_id, count(1) as qtd_visualizacao '+
															'from tb_acesso_artigos group by artigos_id) ac on a.id = ac.artigos_id order by dataCadastro desc'),
	'''
	
	#x = Artigos.objects.select_related('AcessoArtigo').annotate(qtd_visualizacao=Count('acessoartigo')).order_by('-dataCadastro')[:5]
	#print x.query
	context = { "artigos":Artigos.objects.select_related('AcessoArtigo').annotate(qtd_visualizacao=Count('artigos_id')),
			  }
	return render(request, 'index.html', context)


def dictfetchall(cursor):
	"Returns all rows from a cursor as a dict"
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()[0:5]
    ]


def serializeJson(obj):
	obj = serializers.serialize('json', obj)
	return HttpResponse(obj, content_type='application/json')


def artigosRecentes(request):
	rec = Artigos.objects.order_by('-dataCadastro')[:5]
	return serializeJson(rec)


def artigosMaisAcessados(request):
	
	'''cursor = connection.cursor()
	cursor.execute('select a.id, a.titulo, a.slug, ac.qtd_visualizacao from tb_artigos a '+
							 'left join (select artigos_id, count(DISTINCT pcUsuario) as qtd_visualizacao '+
							 'from tb_acesso_artigos group by artigos_id) ac on a.id = ac.artigos_id '+
							 'order by qtd_visualizacao desc')
	row = dictfetchall(cursor)
	row = json.dumps(row, ensure_ascii=False)
	cursor.close()
	return HttpResponse(row, content_type='application/json')
	'''
	
	
	ac = Artigos.objects.select_related('AcessoArtigo').annotate(Count('artigos_id')).order_by('-artigos_id__count')[:5]
	json = '{"json":['
	
	for s in ac:
		json += '{"slug":"' + s.slug + '", "titulo":"'+s.titulo+'", "qtd_visualizacao":'+str(s.artigos_id__count)+'}, '
	if ac:
		json = json[0:len(json)-2]+']}'
	else:
		json +=']}'
	
	return HttpResponse(json, content_type='application/text')


def artigosMaisVotados(request):
	'''
	cursor = connection.cursor()
	cursor.execute('select a.id, a.titulo, a.slug, ra.ranking from tb_artigos a '+
					'left join (select idArtigo_id, SUM(ranking) as ranking from tb_ranking_artigos group by idArtigo_id) ra on a.id = ra.idArtigo_id '+
					'order by ra.ranking desc')
	row = dictfetchall(cursor)
	row = json.dumps(row, ensure_ascii=False)
	cursor.close()
	return HttpResponse(row, content_type='application/json')
	'''
	#mv = Artigos.objects.select_related('RankingArtigo').annotate(Sum('id_artigo'))[:5]
	#mv = Artigos.objects.select_related('RankingArtigo').annotate(Sum('rankingartigo_ranking'))[:5]
	
	#http://stackoverflow.com/questions/7907252/django-orm-select-with-join
	#http://stackoverflow.com/questions/25437078/orm-left-join-query-and-sum
	'''
	r = Artigos.objects.all()
	values = RankingArtigo.objects.filter(idArtigo=r).select_related().annotate(Sum('ranking'))
	print values
	for i in values:
		print i.artigos_slug
	'''
	
	'''
	mv = RankingArtigo.objects.select_related(Artigos).annotate(Sum('ranking')).order_by('-ranking__sum')[:5]
	print mv[0].slug
	'''
	
	rec = Artigos.objects.order_by('-dataCadastro')[:5]
	return serializeJson(rec)
	


def sobre(request):
	return render(request, 'sobre.html')


def contato(request):
	if request.method == 'POST':
		form = ContatoForm(request.POST)
		if not form.is_valid():
			return render(request, 'contato.html', {'form':form} )

		obj = form.save()
		enviarEmailComentario(obj)
		return HttpResponseRedirect('/contato_sucesso/%d/' % obj.pk)
		
	else:
		context = {'form':ContatoForm()}
		return render(request, 'contato.html',  context)


def contato_sucesso(request, pk):
	contato = get_object_or_404(Contatos, pk=pk)
	context = {'contato':contato}
	return render(request, 'contato_sucesso.html', context)
	

def artigo(request, slug):
	objArt = Artigos.objects.filter(slug=slug)[0];
	obj = AcessoArtigo.objects.create(artigos_id=objArt.id,
										ipUsuario = request.META['REMOTE_ADDR'], 
										pcUsuario = request.META['REMOTE_HOST']
										)
	obj.save()
	context = { 'artigos':objArt,
				'ranking':RankingArtigo.objects.filter(idArtigo=objArt.id).aggregate(Sum('ranking'), Avg('ranking')),
				'avaliar':RankingArtigo.objects.filter(ipUsuario = request.META['REMOTE_ADDR'], pcUsuario = request.META['REMOTE_HOST'], idArtigo=objArt.id),}
	return render(request, 'exibeArtigo.html', context)
	

def classifica_artigo(request, pk, rk):
	pk = int(pk)
	objArt = Artigos.objects.filter(id=pk)[0];
	obj = RankingArtigo.objects.create(idArtigo_id=pk, 
										ranking=int(rk), 
										ipUsuario = request.META['REMOTE_ADDR'], 
										pcUsuario = request.META['REMOTE_HOST']
										)
	obj.save()

	return HttpResponse('ok')