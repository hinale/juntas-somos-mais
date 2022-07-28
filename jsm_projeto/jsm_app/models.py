from django.db import models
from django.contrib.auth.models import User
#Os campos de Cliente foram escolhidos de acordo com o que foi observado ser necessario para cadastro no proprio site da JS+. Pensando nisso, deveriamos pensar se fazer um model pra Cliente Fisico e outro pra Juridico seria o correto...levando em conta o site da JS+ (?)
class Cliente(models.Model):
    user = User
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    nascimento = models.DateField()
    profissao = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nome
# Endereço não pode ser apenas um campo de Cliente pois contém muitas informações que precisam ser registrados em um certo padrão pra melhor obtenção(?), validação e leitura dos dados
class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, id)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30) #Poderia ser um choices com lista de estados
    pais = models.CharField(max_length=30) #Poderia ser um choices com lista de paises
#País foi adicionado pq mesmo que a empresa atue apenas no Brasil é, geralmente, esperado que cresçam e alcancem outros paises, ou seja, é adicionado agr para que não precise fazer mudanças futuras no banco de dados

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome