from django.db import models
from .model_product import Product

# todo: connect user model as forign key
class Offer(models.Model):
    STATUS_CHOICE = [
        ("PENDING","Pending" ),
        ("ACCEPTED","Acepted"),
        ("DECLINED","Declined")
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    provider = models.IntegerField()
    datetime = models.DateTimeField()

    # details
    priceperbatch = models.FloatField()
    batchquantity = models.IntegerField()
    unitperbatch = models.IntegerField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="PENDING")

