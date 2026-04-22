from django.db import models
from .model_product import product

class batch(models.Model):
    product_id = models.ForeignKey(
        product,
        on_delete=models.CASCADE,
        db_column="user_id"
    )
    quantity_of_units = models.PositiveIntegerField()
    purchese_price = models.FloatField()
