from django import forms
from .models import Vendor, Product

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['store_name', 'location', 'store_picture', 'qr_picture']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description', 'current_available_amount', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }
