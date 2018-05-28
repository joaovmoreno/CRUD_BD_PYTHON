from django.forms import ModelForm
from .models import *

class DroneForm(ModelForm):
    class Meta():
        model = Drone
        fields = ['status','capacidadeCarga']

class MercadoForm(ModelForm):
    endereco = Endereco
    class Meta():
        model = Mercado
        fields = ['nomeMercado', 'emailMercado', 'telefoneMercado','endereco']

class CategoriaForm(ModelForm):
    class Meta():
        model = Categoria
        fields = ['nomeCategoria']

class ProdutoForm(ModelForm):
   categoria = Categoria
   class Meta():
       model = Produto
       fields = ['nomeProduto','precoProduto','qtdProduto','categoria']