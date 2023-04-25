from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
import re

def chula_email_validator(value):
    pattern = r'@.+.chula.ac.th'
    if not re.search(pattern, value):
        raise ValidationError('Email address must end with chula.ac.th. Example "foo@student.chula.ac.th"')


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True,validators=[chula_email_validator])
    telephone = models.CharField(max_length=10, null=False, unique=True, default='0000000000', validators=[
        RegexValidator(
            regex=r'^0\d{9}$',
            message='Telephone number must start with 0 and have 10 digits',
            code='invalid_telephone'
        )
    ])
    address = models.CharField(max_length=200, null=True,)


    