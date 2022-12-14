from django import forms
from .models import *


class DadosForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF:',
                          widget=forms.TextInput(attrs={'placeholder': 'Digite só os números'}))

    class Meta:
        model = Usuario
        fields = '__all__'


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email']
