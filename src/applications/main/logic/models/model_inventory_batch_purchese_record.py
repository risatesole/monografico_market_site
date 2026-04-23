from django.db import models
from .model_batch import Batch

class InventoryBatchPurchaseRecord(models.Model):

    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name="purchase_records"
    )

    quantity_of_units = models.PositiveIntegerField()
    purchase_price = models.FloatField()