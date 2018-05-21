from django.db import models

import datetime
# Create your models here.

class Endereco(models.Model):
    idEndereco = models.AutoField(primary_key=True)
    quadra = models.CharField(max_length=45, blank=False, null=False)
    alameda = models.CharField(max_length=45, blank=False, null=False)
    lote = models.CharField(max_length=45, blank=False, null=False)
    complemento = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return self.quadra + ' ' + self.alameda + ' ' + self.lote + ' ' + self.complemento

class Mercado(models.Model):
    idMercado = models.AutoField(primary_key=True)
    nomeMercado = models.CharField(max_length=45, blank=False, null=False)
    emailMercado = models.CharField(max_length=100, blank=False, null=False)
    telefoneMercado = models.CharField(max_length=45, blank=False, null=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeMercado

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nomeCliente = models.CharField(max_length=45, blank=False, null=False)
    emailCliente = models.CharField(max_length=100, blank=False, null=False)
    telefoneCliente = models.CharField(max_length=45, blank=False, null=False)

    def  __str__(self):
        return self.nomeCliente

class Drone(models.Model):
    STATUS_CHOICES=(
        ('1','Disponivel'),
        ('2','Indisponivel'),
        ('3','em manutenção')
    )

    idDrone = models.AutoField(primary_key=True)
    status = models.CharField(max_length=45, blank=False, null=False, choices=STATUS_CHOICES)
    capacidadeCarga = models.FloatField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.idDrone

class Tracking(models.Model):
    idTracking = models.AutoField(primary_key=True)
    localizacao = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=100, blank=False, null=False)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)

    def __str__(self):
        return self.localizacao

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nomeCategoria = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return self.nomeCategoria

class Produto(models.Model):
    idProduto = models.AutoField(primary_key=True)
    nomeProduto = models.CharField(max_length=45, blank=False, null=False)
    precoProduto = models.FloatField(max_length=100, blank=False, null=False)
    qtdProduto = models.IntegerField(blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeProduto + ' ' + self.qtdProduto

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    enderecoEntrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    dataPedido = models.DateTimeField(default=datetime.datetime.now())
    valorPedido = models.FloatField(blank=False, null=False)
    qtdProdutos = models.IntegerField(blank=False, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tracking = models.ForeignKey(Tracking, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.idPedido

class FormaPagamento(models.Model):
    PARCELAS_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    )
    TIPO_PAGAMENTO_CHOICES = (
        ('1','credito'),
        ('2','debito')
    )
    idFormaPagamento = models.AutoField(primary_key=True)
    tipoPagamento = models.CharField(max_length=45, blank=False, null=False, choices=TIPO_PAGAMENTO_CHOICES)
    parcelas = models.CharField(max_length=45, blank=False, null=False, choices=PARCELAS_CHOICES)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class ItensPedidos(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    qtdItens = models.IntegerField(blank=False, null=False)
    valorTotal = models.FloatField(blank=False, null=False)

class Mercado_Produto(models.Model):
    mercado = models.ForeignKey(Mercado, on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto)
