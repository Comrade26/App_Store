from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Vendor
from django.contrib import messages
from django.urls import reverse
from .forms import VendorForm, ProductForm

@login_required
def vendor_item(request):
    vendors = Vendor.get_all_vendors()
    vendorID = request.GET.get("vendor")
    if vendorID:
        products = Product.get_all_products_by_vendorid(vendorID)
        vendor = Vendor.objects.get(id=vendorID)
    else:
        products = Product.get_all_products()
        vendor = None

    vendor_product_map = {}
    vendor_product_map["products"] = products
    vendor_product_map["vendors"] = vendors
    vendor_product_map["vendor"] = vendor
    vendor_product_map["vendorID"] = vendorID

    return render(request, "my_products.html", vendor_product_map)


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

@login_required
def add_edit_product(request, product_id=None):
    vendor = request.user.vendor
    if product_id:
        product = get_object_or_404(Product, id=product_id, vendor=vendor)
    else:
        product = None
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor # set the current user as the vendor of the product
            product.save()
            return redirect(f'/buyer/vendor_products/?vendor={request.user.vendor.id}')

    else:
        form = ProductForm(instance=product)
    
    return render(request, 'add_edit_product.html', {'form': form})

@login_required
def delete_product(request, pk):
    product = Product.objects.get(id=pk)

    if request.user.vendor != product.vendor:
        messages.error(request, "You are not authorized to delete this product.")
        return redirect(f'/vendor/my_products/?vendor={request.user.vendor.id}')

    product.delete()
    messages.success(request, "Product has been deleted successfully.")
    return redirect(f'/vendor/my_products/?vendor={request.user.vendor.id}')
