from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('listaclientes', views.listaclientes, name='listaclientes'),
    # FUNCIONAL, MAS NÃO É REQUISITO
    path('categoria', views.categoria, name='categoria'),
    path('produto', views.produto, name='produto'),
    path('produto/editar/<int:id_produto>/', views.editar_produto, name="editar-produto"),
    path('produto/excluir/<int:id_produto>/', views.excluir_produto, name="excluir-poduto"),
    path('visualizarproduto', views.visualizarproduto, name='visualizarproduto'),
    path('pedido', views.pedido, name='pedido'),
    path('pedido/<int:id_produto>/<int:id_cliente>', views.pedido, name='pedido'),
    path('endereco/', views.endereco, name='endereco'),
    path('visualizarpedido/', views.visualizarpedido, name='visualizarpedido'),
    path('login/', views.login, name='login'),
    path('validar_login/', views.validar_login, name='validar_login'),
    path('logout/', views.logout, name='logout'),    
    path('obterproduto/<int:id_produto>', views.obter_produto, name='obter-produto'),
    path('image_upload', views.produto, name = 'image_upload'),
    path('existepedidos/<int:id_produto>', views.existe_pedidos, name = 'existe-pedidos'),
    path('cliente/editar/<int:id_cliente>/', views.editar_cliente, name="editar-cliente"),
    path('cliente/excluir/<int:id_cliente>/', views.excluir_cliente, name="excluir-cliente"),
    path('clientetempedidos/<int:id_cliente>', views.cliente_tem_pedidos, name = 'cliente-tem-pedidos'),
    path('alterarsenha', views.alterar_senha, name = 'alterar-senha')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
