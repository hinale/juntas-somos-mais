from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tkinter import CASCADE


class Usuario(models.Model):
    user = User
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.nome

class Endereco(models.Model):
    cliente = models.ForeignKey(Usuario, id)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    # Poderia ser um choices com lista de estados
    estado = models.CharField(max_length=30)
    # Poderia ser um choices com lista de paises
    pais = models.CharField(max_length=30)
# País foi adicionado pq mesmo que a empresa atue apenas no Brasil é, geralmente, esperado que cresçam e alcancem outros paises, ou seja, é adicionado agr para que não precise fazer mudanças futuras no banco de dados


class Categoria(models.Model):
    nome = models.CharField(max_length=100,  null=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING) #se deletar a  categoria vai ignorar e manter os produtos
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.IntegerField()  # estoque
    destaque = models.BooleanField(
        null=False, default=0)  # produtos em promocao
    figura = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    data = models.DateField(default=timezone.now)
    quantidade = models.IntegerField(default=1)
    valorUnitario = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=30, default='NOVO')

    def __str__(self):
        return self.id
