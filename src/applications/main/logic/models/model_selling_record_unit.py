from django.db import models
from .model_batch import Batch
from .model_unit import Unit

class UnitSellingRecordsUnits(models.Model):
    ENTITY_CHOISES = [
        ("customer", "Customer")
    ]
    datetime = models.DateTimeField()
    unitid = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="unit"
    )
    batchid = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name="batch"
    )
    entity = models.CharField(max_length=20, choices=ENTITY_CHOISES)
    quantity_of_units = models.PositiveIntegerField()
    purchase_price = models.FloatField()

    def __str__(self):
        return None
