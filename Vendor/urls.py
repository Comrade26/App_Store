from django.urls import path
from . import views


app_name = 'vendor'

urlpatterns = [
    path('my_products/', views.vendor_item, name='my_products'),
    path('register/', views.vendor_register, name='vendor_register'),
    path('add-edit-product/', views.add_edit_product, name='add_edit_product'),
    path('add-edit-product/<int:product_id>/', views.add_edit_product, name='edit_product'),
    path('vendor_products/<int:pk>/delete/', views.delete_product, name='delete_product'),
]