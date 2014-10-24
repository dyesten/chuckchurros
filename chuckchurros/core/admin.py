from django.contrib import admin
from chuckchurros.core.models import Artigos, AcessoArtigo, Contatos, Equipe

class ArtigosAdmin(admin.ModelAdmin):
	fieldsets = [
		('Titulo', {'fields':['titulo','slug']}),
		('Artigo', {'fields':['artigo']}),
	]
	prepopulated_fields = {'slug': ('titulo',)}#garante o preenchimento automatico do slug, baseado no nome digitado
	
	exclude = ('user',)
	list_display = ('titulo', 'dataCadastro', 'dataAlteracao', 'artigoAlterado')
	list_filter = ['dataCadastro', 'dataAlteracao', 'titulo']
	search_fields = ['titulo', 'noticia', 'dataCadastro', 'artigoAlterado']
	
	
	def artigoAlterado(self, request):
		return (request.dataAlteracao > request.dataCadastro)
	artigoAlterado.boolean = True
	artigoAlterado.short_description = 'Alterada?'
	
	#salva o pk - id user
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()


class ContatosAdmin(admin.ModelAdmin):
	fieldsets = [
		('Nome', {'fields':['nome',]}),
		('Contato', {'fields':['telefone', 'email']}),
		('Comentario', {'fields':['comentario',]}),
	]
	
	list_display = ('nome', 'telefone', 'email', 'comentario', 'dataCadastro')
	list_filter = ['dataCadastro',]
	search_fields = ['nome', 'dataCadastro']


class EquipeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Membro', {'fields':['nome', 'descricao', 'foto']}),
	]
	
	list_display = ('nome', 'descricao', 'dataCadastro')
	list_filter = ['dataCadastro']
	search_fields = ['nome', 'descricao']
	
	list_per_page = 10

	
admin.site.register(Artigos, ArtigosAdmin)
admin.site.register(Contatos, ContatosAdmin)
admin.site.register(Equipe, EquipeAdmin)
#admin.site.register(AcessoArtigo)