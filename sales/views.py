from django.shortcuts import redirect, render
from sales.models import Sale

from products.carrito import Carrito

# Create your views here.

def confirm_buy(request):


    if request.method == "POST":
        sale = Sale()
        # sale_detail = Sale_detail

        sale.voucher_type = 'boleta'
        sale.tax = '0.18'
        sale.total = int(int(request.POST['total']))
        sale.user =  request.user
        sale.save()
        cart=Carrito(request)
        cart.limpiar()
        return redirect('user:index')
        # request.session["carrito"] = {}
        # request.session.modified = True
    else:
        return render(request,'confirm_buy.html')

    return render(request,'confirm_buy.html')

