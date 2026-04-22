from django.db import models
from .model_product import product
from ...models import User

class inventory_record(models.Model):
    product_id = models.ForeignKey(
        product,
        on_delete=models.CASCADE,
        db_column="product_id"
    )
    recived_at = models.DateTimeField()
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="provided_lots",
        db_column="provider_id"
    )

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="approved_lots",
        db_column="approved_by",
        limit_choices_to={"role": "internal_user"}
    )

    acquisition_cost_per_unit = models.FloatField()
    acquisition_tax = models.FloatField()

    received_at = models.DateTimeField()

    def __str__(self):
        return f"Lot {self.id}"

