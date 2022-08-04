from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dados/', views.dados, name='dados'),
    path('listaclientes', views.listaclientes, name='listaclientes'),
]