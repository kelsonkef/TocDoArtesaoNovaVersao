from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:publicacao_id>', views.publicacao, name='publicacao'),
    path('cadastra_comentario/<int:publicacao_id>', views.comentario_publicacao, name='cadastra_comentario'),
    path('deleta_comentario/<int:comentario_id>', views.deleta_comentario, name='deleta_comentario'),
]
