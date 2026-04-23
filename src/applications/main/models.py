from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Offer(models.Model):
    STATUS_CHOICE = [
        ("PENDING","Pending" ),
        ("ACEPTED","Acepted"),
        ("DECLINED","Declined")
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    providerid = models.IntegerField()
    datetime = models.DateTimeField()
    priceperunit = models.FloatField()
    unitquantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="PENDING")

