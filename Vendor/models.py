from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)  #Product Owner
    name = models.CharField(max_length=255) #Product Name
    price = models.DecimalField(max_digits=10, decimal_places=2) #Product Price
    image = models.ImageField(upload_to='images/') #Product Image
    description = models.TextField() #Product Description
    current_available_amount = models.PositiveIntegerField() #Product Current Amount
    category = models.CharField(max_length=255) #Product Category
    created_at = models.DateTimeField(auto_now_add=True) #Product Created Date
    updated_at = models.DateTimeField(auto_now=True) #Product Updated Date
    is_active = models.BooleanField(default=True) #Product Availability
    is_featured = models.BooleanField(default=False) #Product Best sellers

    def __str__(self):
        return self.name    