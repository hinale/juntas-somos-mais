from dataclasses import fields
from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedido
        fields = '__all__'
