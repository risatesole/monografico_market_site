from .logic.models.model_user import User  as User
from .logic.models.model_user import UserRoles as UserRoles
from .logic.models.model_product import Product as Product 
from django.db import models
class Offer(models.Model):
    STATUS_CHOICE = [
        ("PENDING","Pending" ),
        ("ACCEPTED","Acepted"),
        ("DECLINED","Declined")
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    providerid = models.IntegerField()
    datetime = models.DateTimeField()
    priceperunit = models.FloatField()
    unitquantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="PENDING")

