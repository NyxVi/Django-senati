""" Sales URLs. """

# Django
from django import views
from django.urls import path

from sales.views import confirm_buy
# View
# from products.views import 

urlpatterns = [
    path('confirm_buy/', confirm_buy, name="confirm_buy"),
]