from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dados/', views.dados, name='dados'),
    path('listaclientes', views.listaclientes, name='listaclientes'),
    # FUNCIONAL, MAS NÃO É REQUISITO
    path('categoria', views.categoria, name='categoria'),
    path('produto', views.produto, name='produto'),
    path('visualizarproduto', views.visualizarproduto, name='visualizarproduto'),
    path('pedido', views.pedido, name='pedido'),
    path('visualizarpedido', views.visualizarpedido, name='visualizarpedido'),
]
