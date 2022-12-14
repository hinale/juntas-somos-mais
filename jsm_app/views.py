from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import *
from .models import *
from rest_framework import viewsets
from .serializers import PedidoSerializer, UsuarioSerializer, ProdutoSerializer
from hashlib import sha256
from django.urls import reverse
from django.core import serializers
import json

#Obtém os valores das variáveis de sessão
def obter_usuario_da_sessao(request):
    usuario = {
        "id": request.session.get('usuario'),
        "nome": request.session.get('nome_usuario'),
        "email": request.session.get('email_usuario'),
        "logado": request.session.get('logado'),
    }
    return usuario


def home(request):
    produtos = Produto.objects.all()
    usuario = obter_usuario_da_sessao(request)
    context = {'produtos': produtos, 'usuario': usuario}
    return render(request, "home.html", context)


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
        request.session['nome_usuario'] = usuario[0].nome
        request.session['email_usuario'] = usuario[0].email
        request.session['logado'] = True
        return redirect('/pedido')

    return HttpResponse(f"{email} {senha}")


def logout(request):
    request.session.flush()  # vai deslogar o usuario
    return redirect('/login/')


def cadastro(request):
    status = request.GET.get('status')
    usuario = obter_usuario_da_sessao(request)
    return render(request, 'cadastro.html', {'status': status, 'usuario': usuario})


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
    else:
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
    usuario = obter_usuario_da_sessao(request)
    context = {'form': form, 'usuario': usuario}
    return render(request, 'produto.html', context)


def editar_produto(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('visualizarproduto')
    usuario = obter_usuario_da_sessao(request)
    context = {'produto': produto, 'form': form, 'usuario': usuario}
    return render(request, "editar_produto.html", context)


def visualizarproduto(request):
    produto = Produto.objects.all
    usuario = obter_usuario_da_sessao(request)
    context = {'produto': produto, 'usuario': usuario}
    response = render(request, 'visualizarproduto.html',
                      context)  # django.http.HttpResponse
    return render(request, 'visualizarproduto.html', context)


def listaclientes(request):
    data = Usuario.objects.all()
    usuario = obter_usuario_da_sessao(request)
    clientes = {
        "usuario_number": data,
        "usuario": usuario
    }
    return render(request, 'listaclientes.html', clientes)


def editar_cliente(request, id_cliente):
    cliente = Usuario.objects.get(id=id_cliente)
    form = UsuarioForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listaclientes')
    usuario = obter_usuario_da_sessao(request)
    context = {'cliente': cliente, 'form': form, 'usuario': usuario}
    return render(request, "editar_cliente.html", context)


def excluir_cliente(request, id_cliente):
    cliente = Usuario.objects.get(id=id_cliente)
    cliente.delete()
    return HttpResponseRedirect(reverse('listaclientes'))


def dar_baixa_estoque(form):

    # Pega os produtos a partir da instância do formulário
    id_produto = form['produto'].value()
    quantidade = form['quantidade'].value()

    produto = Produto.objects.get(id=id_produto)
    produto.quantidade = int(produto.quantidade) - int(quantidade)
    produto.save()
    print('Estoque atualizado com sucesso.')


def pedido(request, id_produto=None, id_cliente=None):
    if not request.session.get('usuario'):
        return redirect('/login/?status=2')

    if id_produto and id_cliente:
        produto = Produto.objects.get(id=id_produto)
        initial_data = {
            "cliente": id_cliente,
            "produto": id_produto,
            "valorUnitario": produto.valor
        }
        form = PedidoForm(request.POST or None, initial=initial_data)
    else:
        form = PedidoForm(request.POST or None)

    if form.is_valid():
        form.save()
        dar_baixa_estoque(form)
        form = PedidoForm()
    usuario = obter_usuario_da_sessao(request)
    context = {'form': form, 'usuario': usuario}
    return render(request, 'pedido.html', context)


def endereco(request):
    if request.method == "GET":
        form = EnderecoForm()
        context = {'form': form}
        return render(request, 'endereco.html', context)
    else:
        form = EnderecoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = EnderecoForm()
        context = {'form': form}
        return render(request, 'endereco.html', context)


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


def visualizarpedido(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])

        u = obter_usuario_da_sessao(request)

        # vai filtrar e só aparecer os pedidos do usuario logado
        pedido = Pedido.objects.filter(cliente=usuario)
        return render(request, 'visualizarpedido.html', {'pedido': pedido, 'usuario': u})
    else:
        return redirect('/login/?status=2')


def obter_produto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    data = serializers.serialize('json', [produto, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data)


def excluir_produto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    produto.delete()
    return HttpResponseRedirect(reverse('visualizarproduto'))

#se temos produto relacionado ao pedido
def existe_pedidos(request, id_produto):
    pedido = Pedido.objects.filter(produto_id=id_produto).first()
    if(pedido):
        return JsonResponse({"result": True})
    else:
        return JsonResponse({"result": False})

#se temos cliente relacionado ao pedido
def cliente_tem_pedidos(request, id_cliente):
    pedido = Pedido.objects.filter(cliente_id=id_cliente).first()
    if(pedido):
        return JsonResponse({"result": True})
    else:
        return JsonResponse({"result": False})


def alterar_senha(request):
    usuario = obter_usuario_da_sessao(request)
    context = {'status': 1, 'usuario': usuario}
    return render(request, 'alterar_senha.html', context)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
