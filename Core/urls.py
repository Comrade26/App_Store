from django.urls import path, include
from .views import RegistrationView

app_name = 'Core'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
]
