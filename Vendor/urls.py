from django.urls import path
from . import views


app_name = 'vendor'

urlpatterns = [
    path('my_products/', views.vendor_item, name='my_products'),
    path('register/', views.vendor_register, name='vendor_register'),
    
]