from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("fruit", "Fruit"),
        ("vegetable", "Vegetable"),
        ("clothing", "Clothing"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

