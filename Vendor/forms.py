from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vendor

class VendorRegistrationForm(UserCreationForm):
    store_name = forms.CharField(max_length=50, required=True)
    location = forms.CharField(max_length=100, required=True)
    store_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['store_name', 'location', 'store_picture', 'qr_picture']
