from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

from Core.models import User
from Vendor.models import Product
import datetime
# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
    
    def __str__(self):
                return f'{self.product} {self.customer}'

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

