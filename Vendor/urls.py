from django.contrib import admin
from django.urls import path, re_path
# from .middlewares.auth import auth_middleware
from . import views


app_name = 'vendor'

urlpatterns = [
    path('login/', views.vendor_login, name='vendor_login'),
    path('signup/', views.vendor_signup, name='vendor_signup'),
    path('my_products/', views.vendor_item, name='my_products'),
    path('vendor/register/', views.vendor_register, name='vendor_register'),
    
]