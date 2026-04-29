from django.db import models
from .provider_model import Provider
from ...account.user.models.employee_profile import Employee

class StockEntry(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="receipts"
    )

    provider = models.ForeignKey(
        Provider,
        on_delete=models.SET_NULL,
        null=True,
        related_name="receipts"
    )

    metric_unit = models.CharField(
        max_length=50,
        help_text="unit, pound, bottle, etc."
    )

    quantity = models.PositiveIntegerField()
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    received_at = models.DateTimeField(auto_now_add=True)

    added_by = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    note = models.TextField(blank=True, null=True)

    def total_cost(self):
        return self.quantity * self.cost_per_unit
    