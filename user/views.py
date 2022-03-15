""" Products views """

# Django
import imp
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q

# Models
from user.models import User
from products.models import Product
from sales.models import Sale_detail

# Index home view
def Index(request):    
    
    
    context = {
        'product_order_date' : Product.objects.all().order_by('-date')[:4],
        'x' : Sale_detail.objects.values('product_id').annotate(truck_count=Count('product_id')).order_by('-truck_count'),
        
        # 'f' : Sale_detail.objects.filter(product_id='product_id'),


        # 'product_order_trend1' : Sale_detail.objects.values('product_id').annotate(count=Count('product_id')),
        # 'product_order_trend2' : Sale_detail.objects.all().annotate(count=Count('product_id')),
        'product_order_trend3' : Sale_detail.objects.all().order_by('product_id'),
        # 'f' : Sale_detail.objects.values('product_id').annotate(the_count=Count('product_id'))

    }
    
    return render(request,'index.html', context = context)
    
    
# Login Render view
def LoginRender_view(request):
    """ Login render view """
    return render(request, 'user/login.html')


# Login view
def LoginView(request):
    """ Login view """
    if  request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('user:index')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username and password'})
    
    return render(request, 'user/login.html')


# Signup render view
def SignupRender_view(request):
    """ Signup render view """
    return render(request, 'user/signup.html')

# Signup view
def SignupView(request):
    """ Signup view """
    
    if request.method == "POST":
        user = User()
        user.username = request.POST['username']
        user.email = request.POST['email']
        password = request.POST['password']
        user.set_password(password)
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.image = request.FILES['image']
        user.save()
    else :
        return render(request, 'user/signup.html')
        
    return render(request, 'user/signup.html')


# Logout view
class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """ Logout view """
    pass