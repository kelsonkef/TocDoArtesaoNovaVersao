from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Publicacao, Comentario
from django.contrib import auth, messages
from user.models import Usuario

def index(request):
    #Filtarando e ordenando
    publicacoes = Publicacao.objects.order_by('-data_publicacao').filter(publicada=True) # Select * from publicacao where publicada = True order by data_publicacao desc
    dados = {
        'publicacoes' : publicacoes,
    }
    for publicacao in publicacoes:
        print(publicacao)
    return render(request,"index.html",dados)

def publicacao(request, publicacao_id):
    publicacoes = get_object_or_404(Publicacao, pk=publicacao_id) #Pega o Objeto ou dá erro 404
    comentarios = Comentario.objects.filter(publicacao=publicacao_id)
    publicacoes_a_exibir = {
        'publicacoes': publicacoes,
        'comentarios': comentarios
    }
    return render(request,"publicacao.html", publicacoes_a_exibir)

def buscar(request):
    lista_publicacaos = None
    if 'buscar' in request.GET:# se tem o paramentro buscar dentro do GET
        lista_publicacaos = publicacao.objects.order_by('-data_publicacao').filter(publicada=True)
        nome_da_busca= request.GET['buscar']
        if buscar: #Se buscar tiver preenchido
            lista_publicacaos = lista_publicacaos.filter(nome_publicacao__icontains=nome_da_busca) # o __icontains funciona como um like do SQL
    dados = {
        'publicacaos': lista_publicacaos
    }

    return render(request, 'buscar.html', dados)

def comentario_publicacao(request, publicacao_id):
    if request.method == 'POST':
        titulo_comentario = request.POST['titulo_comentario']
        comentario_texto = request.POST['comentario']
        if campo_vazio(titulo_comentario):
            messages.error(request, 'O titulo do Comentario não pode ficar vazio')
            return  redirect('publicacao',publicacao_id)
        if campo_vazio(comentario_texto):
            messages.error(request, 'O campo comentario não pode ficar vazio')
            return  redirect('publicacao',publicacao_id)
        usuario = get_object_or_404(Usuario,pk=request.user.id)
        publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
        comentario = Comentario.objects.create(publicacao = publicacao, usuario = usuario, titulo = titulo_comentario, descricao= comentario_texto)
        comentario.save()
        return  redirect('publicacao',publicacao_id)
    return  redirect('publicacao',publicacao_id)

def deleta_comentario(request, comentario_id):
    comentario =  get_object_or_404(Comentario, pk = comentario_id)
    publicacao_id = comentario.publicacao.id
    comentario.delete()
    return redirect('publicacao', publicacao_id)

def campo_vazio(campo):
    return not campo.strip()
