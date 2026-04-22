from django.db import models
from .model_product import Product

class Batch(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="batches"
    )

    quantity_of_units = models.PositiveIntegerField()
    purchase_price = models.FloatField()

    def __str__(self):
        return f"Batch of {self.product.name}"
