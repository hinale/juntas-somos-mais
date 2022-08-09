from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha1')
        user = User.objects.filter(email=email).first()
        if user:
            messages.info(request, 'Usuario já cadastrado.')
            return redirect('cadastro')
        user = User.objects.create_user(
            first_name=nome, username=nome, email=email, password=senha)
        user.save()
        return redirect('dados')
       # return HttpResponse("Cadastrado com sucesso") #redirecionar para inserção de dados pessoais (models Cliente) aka dados


def dados(request):
    form = DadosForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DadosForm()
    context = {'form': form}
    return render(request, 'dados.html', context)


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
    data = Cliente.objects.all()
    clientes = {
        "cliente_number": data
    }
    return render(request, 'listaclientes.html', clientes)
