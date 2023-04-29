# from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category, Product, Vendor
from django.contrib import messages
from .forms import VendorForm

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

@login_required
def vendor_register(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.save()
            messages.success(request, 'Your vendor account has been created!')
            return redirect('vendor:my_products')
    else:
        form = VendorForm()
    return render(request, 'vendor_registration.html', {'form': form})
