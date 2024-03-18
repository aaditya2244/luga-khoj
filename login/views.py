from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm  
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import ProductForm  
from .models import Product  
from django.contrib import messages


def index(request):
    return render(request, 'home/index.html')

def admin_page(request):
    return render(request, 'admin/admin.html')

def user_page(request):
    return render(request,'user/user.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)
            return redirect('index') 
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_page')  
                else:
                    return redirect('user_page') 
    else:
        form = AuthenticationForm() 
    return render(request, 'login/login.html', {'form': form})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'admin/add_product.html', {'form': form})

def view_products(request):
    products = Product.objects.all()
    return render(request, 'admin/view_products.html', {'products': products})