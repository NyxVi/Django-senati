# Django
from django.contrib import admin

# Models
from products.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Products admin model """
    list_display = ('product_id', 'name', 'category', 'price', 'stock')
    list_display_links = ('product_id', 'name')
    search_fields = (
        'product_id',
        'name',
        'category',
        'price',
        'stock'
    )
    list_filter = (
        'category',
    )
    