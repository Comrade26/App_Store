from django.urls import path, include
from .views import *

app_name = 'Core'

urlpatterns = [
    path('login/', BuyerLoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
]
