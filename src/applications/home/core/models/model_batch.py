from django.db import models
from .model_product import Product

class Batch(models.Model):
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column="user_id"
    )
    quantity_of_units = models.PositiveIntegerField()
    purchase_price = models.FloatField()
