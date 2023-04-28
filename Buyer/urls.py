from django.urls import path, include
from . import views

app_name = 'Buyer'

urlpatterns = [
    # path('buyer/signup/', views.buyer_signup, name='buyer_signup'),
    # path('buyer/login/', views.buyer_login, name='buyer_login'),
    # path('buyer/profile/', views.buyer_profile, name='buyer_profile'),
    path('category_products/', views.store, name='category_products'),
    path('single_products/', views.item, name='single_products'),
    # path('vendor_products/', views.item, name='vendor_products'),
    path('vendor_products/', views.vendor_item, name='vendor_products'),
    # path('cart/', include('cart.urls', namespace='cart')),
]
