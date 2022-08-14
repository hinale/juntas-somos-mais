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
    path('visualizarproduto', views.visualizarproduto, name='visualizarproduto'),
    path('pedido', views.pedido, name='pedido'),
    path('endereco/', views.endereco, name='endereco'),
    path('visualizarpedido', views.visualizarpedido, name='visualizarpedido'),
    path('login/', views.login, name='login'),
    path('validar_login/', views.validar_login, name='validar_login'),
    path('logout/', views.logout, name='logout'),
    path('get_product_priece', views.get_product_priece, name='get_product_priece'),
    path('image_upload', views.produto, name = 'image_upload')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)