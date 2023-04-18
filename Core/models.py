from django.db import models
from django.contrib.auth.models import AbstractUser
import re

from django.core.exceptions import ValidationError

def chula_email_validator(value):
    pattern = r'@.+.chula.ac.th'
    if not re.search(pattern, value):
        raise ValidationError('Email address must end with chula.ac.th. Example "foo@student.chula.ac.th"')


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True,validators=[chula_email_validator])



    