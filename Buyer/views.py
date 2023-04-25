from django.shortcuts import render
from Vendor.models import Product, Category, Vendor

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

def vendor_item(request):
    vendors = Vendor.get_all_vendors()
    vendorID = request.GET.get("vendor")
    if vendorID:
        products = Product.get_all_products_by_vendorid(vendorID)
    else:
        products = Product.get_all_products()

    vendor_product_map = {}
    vendor_product_map["products"] = products
    vendor_product_map["vendors"] = vendors

    return render(request, "vendor_products.html", vendor_product_map)
