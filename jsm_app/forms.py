from django import forms
from .models import *


class DadosForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF:',
                          widget=forms.TextInput(attrs={'placeholder': 'Digite só os números'}))

    class Meta:
        model = Cliente
        fields = {
            'nome',
            'cpf',
            'telefone',
            'nascimento',
            'profissao'
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
