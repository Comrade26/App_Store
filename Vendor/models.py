from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Vendor(models.Model):
    store_name = models.CharField(max_length=50, null=False)
    user = models.OneToOneField(User, null=False, blank=True, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=10, null=False, unique=True, default='0000000000', validators=[
        RegexValidator(
            regex=r'^0\d{9}$',
            message='Telephone number must start with 0 and have 10 digits',
            code='invalid_telephone'
        )
    ])

    email = models.CharField(max_length=200, null=False, unique=True, default='vendor_email', validators=[
        RegexValidator(
            regex=r'.+@.+.chula.ac.th',
            message='Email must end with "chula.ac.th"',
            code='invalid_email'
        )
    ])

    location = models.CharField(max_length=100)

    store_picture = models.ImageField(upload_to='store_pictures/', null=True)
    qr_picture = models.ImageField(upload_to='qr_picture/', null=True)

    def __str__(self):
        return self.store_name


