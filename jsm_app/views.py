from itertools import product
from django.http import JsonResponse
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *
from rest_framework import viewsets
from .serializers import PedidoSerializer
from hashlib import sha256
from django.contrib.auth.decorators import login_required


def home(request):
    data = Produto.objects.all()
    prod = {"produto_number": data}
    return render(request, "home.html", prod)


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()  # para criptografar a senha

    usuario = Usuario.objects.filter(email=email). filter(senha=senha)

    if len(usuario) == 0:
        return redirect('/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/pedido')

    return HttpResponse(f"{email} {senha}")



def logout(request):
    request.session.flush()  # vai deslogar o usuario
    return redirect('/login/')


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email=email)

    # para verificar se o usuário não colocou a informação solicitada e sim apenas espaços
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/cadastro/?status=1')

    if len(senha) < 8:  # para verificar se a senha tem menos de 8 digitos
        return redirect('/cadastro/?status=2')

    if len(usuario) > 0:  # para verificar se o usuário já existe
        return redirect('/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()  # para criptografar a senha
        usuario = Usuario(nome=nome, senha=senha, email=email)
        usuario.save()

        return redirect('/cadastro/?status=0')
    except:
        return redirect('/cadastro/?status=4')


def categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CategoriaForm()
    context = {'form': form}
    return render(request, 'categoria.html', context)


def produto(request):
    if request.method == "GET":
        form = ProdutoForm()
        context = {'form': form}
        return render(request, 'produto.html', context)
    else:
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
        context = {'form': form}
        return render(request, 'produto.html', context)


def visualizarproduto(request):
    produto = Produto.objects.all
    context = {'produto': produto}
    response = render(request, 'visualizarproduto.html',
                      context)  # django.http.HttpResponse
    return render(request, 'visualizarproduto.html', context)


def listaclientes(request):
    data = Usuario.objects.all()
    clientes = {
        "usuario_number": data
    }
    return render(request, 'listaclientes.html', clientes)

def pedido(request):
    if request.session.get('usuario'):
        form = PedidoForm(request.POST or None)
    else:
        return redirect('/login/?status=2')
    if form.is_valid():
        form.save()
        form = PedidoForm()
    context = {'form': form}
    return render(request, 'pedido.html', context)
    


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


def visualizarpedido(request):
    pedido = Pedido.objects.all
    context = {'pedido': pedido}
    response = render(request, 'visualizarpedido.html',
                      context)  # django.http.HttpResponse
    return render(request, 'visualizarpedido.html', context)

def get_product_priece(request):
    product_id = request.GET.get('product_id', None)
    data = {'product_priece': Produto.objects.get(id=int(product_id)).valor.real}
    return JsonResponse(data)

@property
def valor_total(self):
    return valor_total (Pedido.quantidade * Produto.valor)

