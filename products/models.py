from django.db import models

TypeProducts = [
    ('Limpeza' , 'Limpeza')
]

TypePayment = [
    ('Cartão' , 'Cartão')
]
# Create your models here.
class Product(models.Model):
    name = models.CharField()
    type_product = models.CharField(choices=TypeProducts)
    vr_product = models.DecimalField(max_digits = 5, decimal_places = 2)

class Worker(models.Model):
    name = models.CharField()
    telephone = models.CharField(max_length=11)
    dt_init = models.DateField(auto_now=True)

class Sale(models.Model):
    fk_product = models.ForeignKey(Product, related_name='SaleProduct')
    fk_worker = models.ForeignKey(Worker, related_name='SaleWorker')
    amount = models.IntegerField()
    dtm_sale = models.DateTimeField(auto_now=True)
    type_payment = models.CharField(choices=TypePayment)
