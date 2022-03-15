""" Products Forms """

# Django
from django import forms

# Model
from products.models import Product


class ProductForm(forms.ModelForm):
       class Meta:
           model = Product
           fields = '__all__'

class ProductFormCreate(forms.ModelForm):
       class Meta:
           model = Product
           fields = '__all__'

class ProductFormUpdate(forms.ModelForm):
       class Meta:
           model = Product
           fields = '__all__'