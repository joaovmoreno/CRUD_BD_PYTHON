from django.shortcuts import render, redirect,get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse


from .models import *

class DroneForm(ModelForm):
    class Meta():
        model = Drone
        fields = ['status','capacidadeCarga']


def drone_create(request, template_name='product_form.html'):
    form = DroneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, template_name, {'form': form})


def drone_update(request, drone_id, template_name='product_form.html'):
    drone = get_object_or_404(Drone, pk=drone_id)
    form = DroneForm(request.POST or None, instance=drone)
    if form.is_valid():
        form.save()
        return redirect('/cadastroDrone/')
    return render(request, template_name, {'form': form})


def drone_delete(request, drone_id, template_name='product_confirm_delete.html'):
    drone = get_object_or_404(Drone, pk=drone_id)
    if request.method == 'POST':
        drone.delete()
        return redirect('products')
    return render(request, template_name, {'object': drone})

############################################################################################################
class MercadoForm(ModelForm):
    class Meta():
        model = Mercado
        fields = ['nomeMercado','emailMercado','telefoneMercado']

def mercado_create(request, template_name='product_form.html'):
    form = MercadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, template_name, {'form': form})


def mercado_update(request, mercado_id , template_name='product_form.html'):
    mercado = get_object_or_404(Mercado, pk=mercado_id)
    form = DroneForm(request.POST or None, instance=mercado)
    if form.is_valid():
        form.save()
        return redirect('/cadastroMercado/')
    return render(request, template_name, {'form': form})


def mercado_delete(request, mercado_id, template_name='product_confirm_delete.html'):
    mercado = get_object_or_404(Drone, pk=mercado_id)
    if request.method == 'POST':
        mercado.delete()
        return redirect('products')
    return render(request, template_name, {'object': mercado})

###########################################################################################################
class CategoriaForm(ModelForm):
    class Meta():
        model = Categoria
        fields = ['nomeCategoria']


def categoria_create(request, template_name='product_form.html'):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, template_name, {'form': form})


def categoria_update(request, categoria_id, template_name='product_form.html'):
    categoria = get_object_or_404(Drone, pk=categoria_id)
    form = DroneForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('/cadastroDrone/')
    return render(request, template_name, {'form': form})


def categoria_delete(request, categoria_id, template_name='product_confirm_delete.html'):
    categoria = get_object_or_404(Drone, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('products')
    return render(request, template_name, {'object': categoria})
###########################################################################################################
class ProdutoForm(ModelForm):
   class Meta():
       model = Produto
       fields = ['nomeProduto','precoProduto','qtdProduto','categoria']

def produto_create(request, template_name='product_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, template_name, {'form': form})


def produto_update(request, produto_id, template_name='product_form.html'):
    produto = get_object_or_404(Drone, pk=produto_id)
    form = DroneForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('/cadastroDrone/')
    return render(request, template_name, {'form': form})


def produto_delete(request, produto_id, template_name='product_confirm_delete.html'):
    produto = get_object_or_404(Drone, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('products')
    return render(request, template_name, {'object': produto})

# Create your views here.

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
#################################
        #CRUD DRONE
#################################
# def CadastroDrone(request):
#     return render(request, 'cadastroDrone.html', context=None)
#
# def SalvarDrone(request):
#     status = request.POST.get('status')
#     carga = request.POST.get('carga')
#
#     if status and carga:
#         drone = Drone()
#         drone.status = status
#         drone.capacidadeCarga = carga
#         drone.save()
#         return redirect('/base/')
#     return HttpResponse('<div>'
#                         '<h6>Drone salvo</h6>'
#                         '</div>')
#
def visualizarDrone(request):
    drone = Drone.objects.all()
    return render(request,'visualizarDrone.html', context={'drones':drone})

# def UpdateDrone(request,id_drone):
#     drone = Drone.objects.get(pk = id_drone)
#
#     drone.status = request.POST.get('status')
#     drone.capacidadeCarga = request.POST.get('carga')
#
#     drone._
#
#     return render(request, 'AtualizarDrones.html', context={'drones': drone})
#
#
# def DeleteDrone(request,id_drone):
#     drone = Drone.objects.get(pk=id_drone)
#
#     if request.POST.get('btnDelete'):
#         HttpResponse('<h1>Certeza?</h1>'
#                      '<btn type="subimit" name="sim">Sim</button><button type="subimit" name="nao">Nao</button>')
#         if request.POST.get('Sim'):
#             drone.delete()
#         else:
#             return render(request, 'visualizarDrone.html', context={'drones': drone})
#
#
#     return render(request,'visualizarDrone.html', context={'drones':drone})
#


