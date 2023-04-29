from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User, chula_email_validator


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





