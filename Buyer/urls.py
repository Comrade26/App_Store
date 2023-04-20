from django.urls import path
from .views import BuyerLoginView

urlpatterns = [
    path('login/', BuyerLoginView.as_view(), name='buyer_login'),
]
