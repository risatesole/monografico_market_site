from django.db import models
from .model_product import product
from ...models import User

class inventory_records(models.Model):
    product = models.ForeignKey(
        product,
        on_delete=models.CASCADE,
        related_name="inventory_records"
    )

    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="provided_lots",
        limit_choices_to={"role": "provider"}
    )

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_lots",
        limit_choices_to={"role": "employee"}
    )
    quantity = models.PositiveIntegerField()
    acquisition_cost_per_unit = models.FloatField()
    acquisition_tax = models.FloatField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lot {self.id} - {self.product.name}"