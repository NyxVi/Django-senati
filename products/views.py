""" Products views """

# Django
from ast import Del
from itertools import product
from math import prod
import re
from statistics import mode
from unicodedata import category
from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls.base import reverse_lazy
from django.db.models import Q

# Models
from products.models import Product

# Forms
from products.forms import ProductFormCreate, ProductFormUpdate, ProductForm

# Utilities
from products.carrito import Carrito


class ProductsListView(ListView):
    """ Return all products """
    template_name = 'product/list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsCreateView(CreateView):
    """ Produts create view """
    template_name = 'product/create.html'
    form_class  = ProductForm
    success_url = reverse_lazy('product:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsUpdateView(UpdateView):
    """ Products update view """
    model = Product
    template_name = 'product/update.html'
    form_class  = ProductForm
    success_url = reverse_lazy('product:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsDeleteView(DeleteView):
    """ Products delete view """
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product:list')


def DetailProductView(request, pk):
    """ Detail product View """
    producto = get_object_or_404(Product, product_id=pk)
    return render(request,'product_detail.html',{'product' : producto})


def ListFilterProductView(request):
    """ List Fileter Product View """
    queryset = request.GET.get("buscar")
    product = Product.objects.all()
    if queryset:
        product = Product.objects.filter(
            Q(name__icontains = queryset) |
            Q(description__icontains = queryset) |
            Q(category__icontains = queryset)
        ).distinct()
        
    context = {
        'product' : product
    }    
    
    return render(request, 'list_filter_product.html',context)

def ListCategoryProduct(request, categ):
    """ List category product """
    product = Product.objects.filter(category=categ)
    
    context={
        'product':product
    }
    
    return render(request, 'list_filter_product.html',context)











################################################################
################################################################

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto= Product.objects.get(product_id=producto_id)
    carrito.agregar(producto)
    context = {
        'carrito' : carrito
    }
    return render(request,'home.html', context = context)
    # return redirect("user:index")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(product_id=producto_id)
    carrito.restar(producto)
    context = {
        'carrito' : carrito
    }
    return render(request,'home.html', context = context)

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto= Product.objects.get(product_id=producto_id)
    carrito.eliminar(producto)
    context = {
        'carrito' : carrito
    }
    return render(request,'home.html', context = context)
    # return redirect("user:index")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    context = {
        'carrito' : carrito
    }
    return render(request,'home.html', context = context)
    # return redirect("user:index")
    
def guardar_carrito(request):
    carrito = Carrito(request)
    carrito.guardar_carrito()
    context = {
        'carrito' : carrito
    }
    return render(request,'home.html', context = context)    