from django.urls import path
from . import views
from .views import ProductCategoryView

urlpatterns = [
    # path('buyer/signup/', views.buyer_signup, name='buyer_signup'),
    # path('buyer/login/', views.buyer_login, name='buyer_login'),
    # path('buyer/profile/', views.buyer_profile, name='buyer_profile'),
    path('category_products/', views.category_products, name='category_products'),
    path('category/<str:category_name>/', ProductCategoryView.as_view(), name='product_category'),
]