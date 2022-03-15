""" Products models """

# Django
from django.db import models



class Product(models.Model):
    """ Product model """
    product_id = models.CharField(primary_key=True, unique=True, max_length=20, blank=False)
    CATEGORY_OPTIONS = (
        ('Tecnologia', 'Tecnologia'),
        ('Ropa', 'Ropa'),
        ('Gaming', 'Gaming'),
        ('Otros', 'Otros')
    )
    category = models.CharField(max_length=20, choices=CATEGORY_OPTIONS, blank=False)
    name = models.CharField(max_length=250)
    description  = models.TextField(blank=True, max_length=250 ,null=True)
    price = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now=True, blank=False, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    
    def __str__(self):
        return self.name

