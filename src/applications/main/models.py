from django.db import models

class Product(models.Model):
    CATEGORY_CHOICE=[
        ("LACTEOS","Lacteos"),
        ("CARNES","carnes"),
        ("VINOS","Vinos")
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICE
    )
    
    def __str__(self):
        return self.name

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

