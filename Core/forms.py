from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, chula_email_validator


class RegistrationForm(UserCreationForm):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(
        max_length=254,
        help_text='Email address must end with chula.ac.th. Example "foo@student.chula.ac.th".',
        validators=[chula_email_validator],
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()

        return user





