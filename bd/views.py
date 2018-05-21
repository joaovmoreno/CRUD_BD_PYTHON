from django.shortcuts import render
from .models import *

# Create your views here.

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

def CadastroDrone(request):
    return render(request, 'cadastroDrone.html', context=None)

def SalvarDrone(request):
    status = request.POST.get('status')
    carga = request.POST.get('carga')

    if status:
        drone = Drone
        drone.status = status
        drone.capacidadeCarga = carga
        drone.save()
        return showbase()

def visualizarDrone(request):
    drone = Drone.objects.all()

    return