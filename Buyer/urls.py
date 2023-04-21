from django.urls import path
from .views import BuyerLoginView

app_name = 'Buyer'

urlpatterns = [
    path('login/', BuyerLoginView.as_view(), name='login'),
]
