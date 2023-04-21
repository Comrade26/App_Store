from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from django.shortcuts import render, redirect
from Vendor.models import Product, Category
from django.views.generic import ListView

# Create your views here.
def store(request):
    categories = Category.get_all_categories()
    categoryID = request.GET.get("category")
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    category_product_map = {}
    category_product_map["products"] = products
    category_product_map["categories"] = categories

    return render(request, "category_products.html", category_product_map)

def item(request):
    productID = request.GET.get("product")
    products = Product.get_products_by_id(productID)

    product_map = {}
    product_map["products"] = products

    return render(request, "single_products.html", product_map)
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             customer = Customer.objects.create(
#                 user=user,
#                 phone_number=request.POST.get('phone_number'),
#                 address=request.POST.get('address'),
#                 city=request.POST.get('city'),
#                 state=request.POST.get('state'),
#                 country=request.POST.get('country'),
#             )
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# def buyer_login(request):
#     if request.method == 'POST':
#         form = BuyerLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('buyer_profile')
#     else:
#         form = BuyerLoginForm()
#     return render(request, 'buyer_login.html', {'form': form})

# def buyer_logout(request):
#     logout(request)
#     return redirect('home')