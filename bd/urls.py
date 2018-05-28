from django.urls import path
from .views import *

urlpatterns = [
    path('base/', showbase, name='list_products'),
    path('listdrone/',list_drone, name='list_drone'),
    path('newdrone/', create_drone, name='create_drone'),
    path('updatedrone/<int:id>/', update_drone, name='update_drone'),
    path('deletedrone/<int:id>/', delete_drone, name='delete_drone'),

    path('listmercado/',list_mercado, name='list_mercado'),
    path('newmercado/', create_mercado, name='create_mercado'),
    path('updatemercado/<int:id>/', update_mercado, name='update_mercado'),
    path('deletemercado/<int:id>/', delete_mercado, name='delete_mercado'),

    path('listproduto/', list_produto, name='list_produto'),
    path('newproduto/', create_produto, name='create_produto'),
    path('updateproduto/<int:id>/', update_produto, name='update_produto'),
    path('deleteproduto/<int:id>/', delete_produto, name='delete_produto'),

    path('listcategoria/', list_categoria, name='list_categoria'),
    path('newcategoria/', create_categoria, name='create_categoria'),
    path('updatecategoria/<int:id>/', update_categoria, name='update_categoria'),
    path('deletecategoria/<int:id>/', delete_categoria, name='delete_categoria'),


]


# CRUD - CREATE, READ, UPDATE, DELETE