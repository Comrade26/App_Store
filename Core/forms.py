from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User, chula_email_validator
from Vendor.models import Vendor


class RegistrationForm(UserCreationForm):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    telephone = models.CharField(max_length=10, null=False, unique=True, validators=[
        RegexValidator(
            regex=r'^0\d{9}$',
            message='Telephone number must start with 0 and have 10 digits',
            code='invalid_telephone'
        )
    ])
    email = forms.EmailField(
        max_length=254,
        help_text='Email address must end with chula.ac.th. Example "foo@student.chula.ac.th".',
        validators=[chula_email_validator],
    )
    address = models.CharField(max_length=200, null=True,)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'telephone', 'email', 'address', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()
        return user

class EditProfileForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'telephone', 'address']

class EditVendorForm(forms.ModelForm):
    store_name = forms.CharField(max_length=100, required=True)
    location = forms.CharField(max_length=100, required=True)
    store_picture = forms.ImageField(required=False)
    qr_picture = forms.ImageField(required=False)

    class Meta:
        model = Vendor
        fields = ['store_name', 'location', 'store_picture', 'qr_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['store_name'].initial = instance.store_name
            self.fields['location'].initial = instance.location
            self.fields['store_picture'].initial = instance.store_picture
            self.fields['qr_picture'].initial = instance.qr_picture

    def save(self, commit=True):
        vendor = super().save(commit=False)
        vendor.store_name = self.cleaned_data['store_name']
        vendor.location = self.cleaned_data['location']
        vendor.store_picture = self.cleaned_data['store_picture']
        vendor.qr_picture = self.cleaned_data['qr_picture']
        if commit:
            vendor.save()
        return vendor