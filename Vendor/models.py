from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.
class Vendor(models.Model):
    store_name = models.CharField(max_length=50, null=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, blank=True, on_delete=models.CASCADE, default=None)
    # first_name = models.CharField(max_length=50, null=False)
    # last_name = models.CharField(max_length=50, null=False)
    # phone = models.CharField(max_length=10, null=False, unique=True, default='0000000000', validators=[
    #     RegexValidator(
    #         regex=r'^0\d{9}$',
    #         message='Telephone number must start with 0 and have 10 digits',
    #         code='invalid_telephone'
    #     )
    # ])

    # email = models.CharField(max_length=200, null=False, unique=True, default='vendor_email', validators=[
    #     RegexValidator(
    #         regex=r'.+@.+.chula.ac.th',
    #         message='Email must end with "chula.ac.th"',
    #         code='invalid_email'
    #     )
    # ])

    location = models.CharField(max_length=100)

    store_picture = models.ImageField(upload_to='images/store_picture/', null=True)
    qr_picture = models.ImageField(upload_to='images/qr_picture/', null=True)

    def __str__(self):
        return self.store_name

class Category(models.Model):
        name = models.CharField(max_length=255)

        @staticmethod
        def get_all_categories():
                return Category.objects.all()

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
        is_active = models.BooleanField(default=True) #Product Availability
        is_featured = models.BooleanField(default=False) #Product Best sellers

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

        def __str__(self):
                return self.name 
