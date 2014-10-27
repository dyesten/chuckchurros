# coding: utf-8
from django.core.mail import send_mail
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, TemplateView, CreateView
from django.db.models import Avg, Sum, Count
from django.db import connection
#import json


from chuckchurros.core.forms import ContatoForm
from chuckchurros.core.models import Artigos, Contatos, RankingArtigo, AcessoArtigo, Equipe


def enviarEmailComentario(obj):	
	titulo = 'Novo mensagem recebida pelo site'
	destino = 'dyesten.pt@gmail.com'
	texto = "\nNome: "+(obj.nome)+" \nE-mail: "+(obj.email)+" \nMensagem: "+(obj.comentario)
	
	send_mail(subject=titulo, message=texto, from_email=destino, recipient_list=[destino],	)


def home(request):
	context = { "artigos":Artigos.objects.qtdVisualizacao,}
	return render(request, 'index.html', context)

'''
def dictfetchall(cursor):
	"Returns all rows from a cursor as a dict"
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()[0:5]
    ]
'''

def serializeJson(obj):
	obj = serializers.serialize('json', obj)
	return HttpResponse(obj, content_type='application/json')


def artigosRecentes(request):
	rec = Artigos.objects.order_by('-dataCadastro')[:5]
	#rec = Artigos.objects.top5Recentes
	
	return serializeJson(rec)


def artigosMaisAcessados(request):
	ac = Artigos.objects.select_related('AcessoArtigo').annotate(Count('artigos_id')).order_by('-artigos_id__count')[:5]
	#ac = Artigos.top5Acessadas.all()
	
	json = '{"json":['+''.join('{"slug":"' + s.slug + '", "titulo":"'+s.titulo+'", "qtd":'+str(s.artigos_id__count)+'}, ' for s in ac)	
	json = json[0:len(json)-2]+']}' if ac else json+']}'
	
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
		
	rec = Artigos.objects.order_by('-dataCadastro')[:5]
	return serializeJson(rec)
	

def sobre(request):
	return render(request, 'sobre.html', {'equipe':Equipe.objects.membros})


class ContatoCreate(CreateView):
	model = Contatos
	form_class = ContatoForm

class ContatoSucesso(DetailView):
	model = Contatos

def artigo(request, slug):
	objArt = Artigos.objects.filter(slug=slug)[0];
	obj = AcessoArtigo.objects.create(artigos_id=objArt.id,
										ipUsuario = request.META['REMOTE_ADDR'], 
										pcUsuario = request.META['SERVER_NAME']
										)
	obj.save()
	context = { 'artigos':objArt,
				'ranking':RankingArtigo.objects.filter(idArtigo=objArt.id).aggregate(Sum('ranking'), Avg('ranking')),
				'avaliar':RankingArtigo.objects.filter(ipUsuario = request.META['REMOTE_ADDR'], pcUsuario = request.META['SERVER_NAME'], idArtigo=objArt.id),}
	return render(request, 'exibeArtigo.html', context)
	

def classifica_artigo(request, pk, rk):
	pk = int(pk)
	objArt = Artigos.objects.filter(id=pk)[0];
	obj = RankingArtigo.objects.create(idArtigo_id=pk, 
										ranking=int(rk), 
										ipUsuario = request.META['REMOTE_ADDR'], 
										pcUsuario = request.META['SERVER_NAME']
										)
	obj.save()
	return HttpResponse('ok')