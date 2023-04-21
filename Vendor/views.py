# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Product, Vendor

def vendor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_vendor:
                login(request, user)
                return redirect('vendor_dashboard')
            else:
                return render(request, 'vendor/login.html', {'error_message': 'You are not a vendor.'})
        else:
            return render(request, 'vendor/login.html', {'error_message': 'Invalid login credentials.'})
    else:
        return render(request, 'login.html')

def vendor_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_vendor = True
            user.save()
            login(request, user)
            return redirect('vendor_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def vendor_item(request):
    vendors = Vendor.get_all_vendors()
    vendorID = request.GET.get("vendor")
    categories = Category.get_all_categories()
    categoryID = request.GET.get("category")
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    vendor_category_product_map = {}
    vendor_category_product_map["products"] = products
    vendor_category_product_map["categories"] = categories
    vendor_category_product_map["vendors"] = vendors

    return render(request, "my_products.html", vendor_category_product_map)


