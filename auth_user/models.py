from django.db import models
from products.models import Products
from datetime import date


# Create your models here.
class Client(models.Model):
    name = models.CharField()
    telephone = models.CharField(max_length=11)
    dt_init = models.DateField(auto_now=True)


class Address(models.Model):
    city = models.CharField()
    neighborhood = models.CharField()
    road = models.CharField()
    number = models.IntegerField()
    fk_client = models.ForeignKey(Client, related_name='AddressClient', on_delete=models.CASCADE)

class Account(models.Model):
    fk_client = models.ForeignKey(Client, related_name='AccountsClient', on_delete=models.CASCADE)
    fk_product = models.ForeignKey(Products, related_name='AccountsProduct', on_delete=models.CASCADE)
    it_paid = models.BooleanField(default=False)
    ammount = models.IntegerField()
