""" Products URLs. """

# Django
from django import views
from django.urls import path

# View
from products.views import *

urlpatterns = [
    
    # path list products
    path(
        route = '',
        view = ProductsListView.as_view(),
        name = 'list'
    ),

    # path create products
    path(
        route = 'create/',
        view = ProductsCreateView.as_view(),
        name = 'create'
    ),

    # path update products
    path(
        route = 'update/<str:pk>',
        view = ProductsUpdateView.as_view(),
        name = 'update'
    ),

    # path delete products
    path(
        route = 'delete/<str:pk>',
        view = ProductsDeleteView.as_view(),
        name = 'delete'
    ),
    
    # path product detail
    path(
        route = 'detail_product/<str:pk>',
        view = DetailProductView,
        name = 'detail_product'
    ),

    # path product list filter
    path(
        route = 'list_filter_product/',
        view = ListFilterProductView,
        name = 'list_filter_product'
    ),

    # path product list category
    path(
        route = 'list_category_product/<str:categ>',
        view = ListCategoryProduct,
        name = 'list_category_product'
    ),


##############

    path('agregar/<str:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<str:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<str:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

    path('guardar/', guardar_carrito, name="Sav"),

]

