from django.shortcuts import render, redirect, HttpResponseRedirect
from Vendor.models import Product, Category, Vendor
from django.views import View
from django.urls import reverse

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

def store(request):
    cart = request.session.get("cart")
    if not cart:
        request.session["cart"] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get("category")
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data["products"] = products
    data["categories"] = categories

    return render(request, "category_products.html", data)
    

class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        # return redirect('')
        return redirect('Buyer:homepage')
    

    def get(self , request):
        print(f"{request.get_full_path()}")
        # return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
        return HttpResponseRedirect(f'category_products'+f"{request.get_full_path().split('buyer/')[1]}")

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )
    

class Single_Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        # return redirect('')
        return redirect('Buyer:singlehomepage')


    def get(self , request):
        print(f"{request.get_full_path()}")
        # return HttpResponseRedirect(f'/buyer/single_products{request.get_full_path()[1:]}')
        return HttpResponseRedirect(f'single_products/{request.GET.get("product")}'+f"{request.get_full_path().split('buyer/')[1]}")
    
def single_store(request):
    cart = request.session.get("cart")
    if not cart:
        request.session["cart"] = {}

    productID = request.GET.get("product")
    products = Product.get_products_by_id(productID)

    product_map = {}
    product_map["products"] = products

    return render(request, "single_products.html", product_map)

def search(request):
    q=request.GET['q']
    data=Product.objects.filter(name__icontains=q)
    return render(request, 'search.html', {'data':data})

