from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.

class Customer(models.Model):
    # username = models.CharField(max_length=200, null=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, blank=True, on_delete=models.CASCADE, default=None)
    # first_name = models.CharField(max_length=200, null=False, default='fname')
    # last_name = models.CharField(max_length=200, null=False, default='lname')
    # password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10, null=False, unique=True, default='0000000000', validators=[
        RegexValidator(
            regex=r'^0\d{9}$',
            message='Telephone number must start with 0 and have 10 digits',
            code='invalid_telephone'
        )
    ])
    # email = models.CharField(max_length=200, null=False, unique=True, default='mail', validators=[
    #     RegexValidator(
    #         regex=r'.+@.+.chula.ac.th',
    #         message='Email must end with "chula.ac.th"',
    #         code='invalid_email'
    #     )
    # ])
    address = models.CharField(max_length=200, null=True,)
