from django.shortcuts import render, redirect
from .models import *
from .forms import *


def list_drone(request):
    drone = Drone.objects.all()
    return render(request, 'list_drone.html', {'drone': drone})


def create_drone(request):
    form = DroneForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_drone')

    return render(request, 'drone_form.html', {'form': form})


def update_drone(request, id):
    drone = Drone.objects.get(pk=id)
    form = DroneForm(request.POST or None, instance=drone)

    if form.is_valid():
        form.save()
        return redirect('list_drone')

    return render(request, 'drone_form.html', {'form': form, 'drone': drone})


def delete_drone(request, id):
    drone = Drone.objects.get(pk = id)

    if request.method == 'POST':
        drone.delete()
        return redirect('list_products')

    return render(request, 'confirm_delete_drone.html', {'drone': drone})
##############################################################################################

def list_mercado(request):
    mercado = Mercado.objects.all()
    return render(request, 'list_mercado.html', {'mercado': mercado})


def create_mercado(request):
    form = MercadoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_mercado')

    return render(request, 'mercado_form.html', {'form': form})


def update_mercado(request, id):
    mercado = Mercado.objects.get(pk=id)
    form = MercadoForm(request.POST or None, instance=mercado)

    if form.is_valid():
        form.save()
        return redirect('list_mercado')

    return render(request, 'mercado_form.html', {'form': form, 'mercado': mercado})


def delete_mercado(request, id):
    mercado = Mercado.objects.get(pk = id)

    if request.method == 'POST':
        mercado.delete()
        return redirect('list_products')

    return render(request, 'confirm_delete_mercado.html', {'mercado': mercado})

##########################################################################################
def list_produto(request):
    produto = Produto.objects.all()
    return render(request, 'list_produto.html', {'produto': produto})


def create_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_produto')

    return render(request, 'produto_form.html', {'form': form})


def update_produto(request, id):
    produto = Produto.objects.get(pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('list_produto')

    return render(request, 'produto_form.html', {'form': form, 'produto': produto})


def delete_produto(request, id):
    produto = Produto.objects.get(pk = id)

    if request.method == 'POST':
        produto.delete()
        return redirect('list_produto')

    return render(request, 'confirm_delete_produto.html', {'produto': produto})

##############################################################################################

def list_categoria(request):
    categoria = Categoria.objects.all()
    return render(request, 'list_categoria.html', {'categoria': categoria})


def create_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_categoria')

    return render(request, 'categoria_form.html', {'form': form})


def update_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('list_categoria')

    return render(request, 'categoria_form.html', {'form': form, 'categoria': categoria})


def delete_categoria(request, id):
    categoria = Categoria.objects.get(pk = id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('list_products')

    return render(request, 'confirm_delete_produto.html', {'categoria': categoria})

##########################################################################################################
def showbase(request):
    pedidos = Pedido.objects.all()
    produtos = Produto.objects.all()
    cliente = Cliente.objects.all()
    mercado = Mercado.objects.all()

    countPedidos = 0
    countProdutos = 0
    countClientes = 0
    countMercado = 0

    for qtd in pedidos:
        countPedidos  = countPedidos + 1
        print (qtd)

    for qtd in produtos:
        countProdutos = countProdutos + 1
        print(qtd)

    for qtd in mercado:
        countMercado = countMercado + 1
        print(qtd)

    for qtd in cliente:
        countClientes = countClientes + 1
        print(qtd)

    return render(request,'base.html',context={'qtdClientes':countClientes,
                                               'qtdPedidos':countPedidos,
                                               'qtdProdutos':countProdutos,
                                               'qtdMercado':countMercado})

