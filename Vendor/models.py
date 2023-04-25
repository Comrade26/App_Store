from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.
class Vendor(models.Model):
        store_name = models.CharField(max_length=50, null=False)
        user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, blank=True, on_delete=models.CASCADE, default=None)
        location = models.CharField(max_length=100)
        store_picture = models.ImageField(upload_to='images/store_picture/', null=True)
        qr_picture = models.ImageField(upload_to='images/qr_picture/', null=True)

        @staticmethod
        def get_all_vendors():
                return Vendor.objects.all()
                
        def __str__(self):
                return self.store_name

class Category(models.Model):
        name = models.CharField(max_length=255)

        @staticmethod
        def get_all_categories():
                return Category.objects.all()
        
        @staticmethod
        def get_all_categories_by_vendorid(vendor_id):
                if vendor_id:
                        return Category.objects.filter(vendor=vendor_id)
                else:
                        return Category.get_all_categories()

        def __str__(self):
                return self.name 
        
class Product(models.Model):
        vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)  #Product Owner
        name = models.CharField(max_length=255) #Product Name
        price = models.DecimalField(max_digits=10, decimal_places=2) #Product Price
        image = models.ImageField(upload_to='images/product/') #Product Image
        description = models.TextField() #Product Description
        current_available_amount = models.PositiveIntegerField() #Product Current Amount
        category = models.ForeignKey(Category, on_delete=models.CASCADE) #Product Category
        created_at = models.DateTimeField(auto_now_add=True) #Product Created Date
        updated_at = models.DateTimeField(auto_now=True) #Product Updated Date

        @staticmethod
        def get_products_by_id(ids):
                return Product.objects.filter(id__in=ids)

        @staticmethod
        def get_all_products():
                return Product.objects.all()

        @staticmethod
        def get_all_products_by_categoryid(category_id):
                if category_id:
                        return Product.objects.filter(category=category_id)
                else:
                        return Product.get_all_products()
                
        @staticmethod
        def get_all_products_by_vendorid(vendor_id):
                if vendor_id:
                        return Product.objects.filter(vendor=vendor_id)
                else:
                        return Product.get_all_products()
                
        
        def __str__(self):
                return self.name 
