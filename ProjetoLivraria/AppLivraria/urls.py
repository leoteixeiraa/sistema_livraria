from django.urls.conf import path
from AppLivraria.views import Index, CriaLivro, ListaLivro, AtualizaLivro,\
    DeletaLivro
from AppLivraria.models import Livro

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('livraria/cadastrar/', CriaLivro.as_view(model=Livro), 
         name="cadastra_livro"),  
    path('livraria/listar/', ListaLivro.as_view(), name="lista_livros"),  
    path('livraria/atualizar/<pk>', AtualizaLivro.as_view(model=Livro),
         name="atualiza_livro"), 
    path('livraria/exclui/<pk>', DeletaLivro.as_view(model=Livro),
         name="deleta_livro") 
]