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
    image = models.ImageField(upload_to="products/", null=True, blank=True)  
    def __str__(self):
        return self.name
