from django import forms
from .models import Vendor

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['store_name', 'location', 'store_picture', 'qr_picture']
