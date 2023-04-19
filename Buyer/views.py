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
def category_products(request):
    categories = Category.objects.all()
    category_product_map = {}
    for category in categories:
        products = Product.objects.filter(category=category)
        category_product_map[category.name] = products
    return render(request, 'category_products.html', {'category_product_map': category_product_map})

class ProductCategoryView(ListView):
    template_name = 'products_by_category.html'  # the template to use
    context_object_name = 'products'  # the name of the queryset in the template
    paginate_by = 10  # the number of items to display per page

    def get_queryset(self):
        # retrieve the category slug from the URL
        category_name = self.kwargs.get('category_name', None)
        
        # retrieve the category object using the slug
        category = Category.objects.get(name=category_name)

        # filter the products by the category
        queryset = Product.objects.filter(category=category)

        return queryset
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