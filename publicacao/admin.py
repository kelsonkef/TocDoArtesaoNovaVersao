from django.contrib import admin
from .models import Publicacao

# Register your models here.
'''
Essa classe funciona como um modelo de como o Django admin deve exibir os dados da Classe Receita.
Vale resaltar que so conseguimos criar filtros, list_diplay e as demais funções com os atributos presentes na classe Receita. 
'''
class ListandoPublicacoes(admin.ModelAdmin):
    list_display = ('id', 'nome_publicacao', 'categoria', 'publicada') # Defini quais serão os atributos que serão exibidos da receita na tabela. 
    list_display_links = ('id', 'nome_publicacao') # Informamos quais campos serão usados para acessar a receita para modificala.(criando um link)
    search_fields = ('nome_publicacao', )# Cria um campo de pesquisa, e qual sera o campo que iremos procurar.
    list_filter = ('categoria', ) #Cria um filtro com o campo que queremos, nesse caso o campo categoria.
    list_editable = ('publicada',)
    list_per_page = 2 # Informa a quantidade de linha que estarão na pagina, cria uma paginação.
    
admin.site.register(Publicacao, ListandoPublicacoes) #Dizendo que eu quero quer o modulo de Admin possa usar, altera a classe Receita