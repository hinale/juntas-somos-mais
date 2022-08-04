from django import forms
from .models import Cliente


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