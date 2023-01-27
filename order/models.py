from django.db import models

from account.models import CustomUser
from product.models import Product
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='address', blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOreder(self):
        self.save()


