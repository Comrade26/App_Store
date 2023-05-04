from django.urls import path, include
from .views import *
from . import views

app_name = 'Core'

urlpatterns = [
    path('login/', BuyerLoginView.as_view(), name='login'),
    path('logout/', views.my_logout_view, name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]
