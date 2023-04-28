from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from Vendor.models import Product, Category, Vendor
from django.views import View

# Create your views here.

# def store(request):
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get("category")
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products()

#     category_product_map = {}
#     category_product_map["products"] = products
#     category_product_map["categories"] = categories

#     return render(request, "category_products.html", category_product_map)

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

# def homePage(request):
        
#     if request.method == 'POST':
#         product = request.POST.get('product')
#         cart = request.session.get('cart')
#         if cart:
#             quantity = cart.get(product)
#             if quantity:
#                 cart[product] = quantity + 1
#             else:
#                 cart[product] = 1
#         else:
#             cart = {}
#             cart[product] = 1

#         cart  =  request.session.get('cart')
#         if not cart:
#             request.session.cart = {}
#         request.session['cart'] = cart
#         # print(request.session['cart'])
#         return redirect('category_products')

#     else:
#         products = None 
#         categories = Category.objects.all()
#         category_id = request.GET.get('category')
#         if category_id:
#             products = Product.objects.filter(category=category_id)
#         else:
#             products = Product.objects.filter(category=1)
#         context = {'products': products, 'categories': categories}
#         # print("Your Email Address is: ", request.session.get('email'))
#         return render(request, 'category_products.html', context)
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
        return redirect('category_products')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    category_product_map = {}
    category_product_map['products'] = products
    category_product_map['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'category_products.html', category_product_map)
    