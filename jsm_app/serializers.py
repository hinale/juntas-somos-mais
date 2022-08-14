from dataclasses import fields
from rest_framework import serializers
from .models import Pedido, Usuario, Produto


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedido
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuario
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = Produto
        fields = '__all__'
