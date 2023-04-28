from django.urls import path
from . import views
from .views import Index ,store, Single_Index,single_store


app_name = 'Buyer'

urlpatterns = [

    # path('single_products/', views.item, name='single_products'),
    # path('vendor_products/', views.item, name='vendor_products'),
    path('vendor_products/', views.vendor_item, name='vendor_products'),
    # path('index/', Index.as_view(), name='homepage'),
    # path('', Index.as_view(), name='homepage'),
    path('', Index.as_view(), name='homepage'),
    # path('category_products/', Index.as_view(), name='homepage'),
    # path('store', store , name='store'),
    path('category_products/', store , name='store'),

    path('', Single_Index.as_view(), name='singlehomepage'),
    path('single_products/', single_store , name='singlestore'),


]
