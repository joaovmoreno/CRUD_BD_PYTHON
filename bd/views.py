from django.shortcuts import render, redirect
from django.http import HttpResponse


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

    if status and carga:
        drone = Drone()
        drone.status = status
        drone.capacidadeCarga = carga
        drone.save()
        return redirect('/base/')
    return HttpResponse('<div>'
                        '<h6>Drone salvo</h6>'
                        '</div>')

def visualizarDrone(request):
    drone = Drone.objects.all()
    return render(request,'visualizarDrone.html', context={'drones':drone})


def UpdateDrone(request,pk):
    drone = Drone()

    status = request.POST.get('status')
    carga = request.POST.get('craga')

    drone.status = status
    drone.capacidadeCarga = carga




    return render(request, 'AtualizarDrones.html', context=None)

def DeleteDrone(request,pk):
    drone = Drone.objects.filter(idDrone=pk).delete()
    drone.save()


