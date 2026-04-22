from django.db import models
from .model_product import product
from ...models import User

class InventoryMovement(models.Model):
    """
    Represents a stock movement event for a product.

    This model is the single source of truth for inventory changes.
    Each record indicates whether stock was added ("in") or removed ("out"),
    along with the reason and context of the movement.

    Inventory movements are used to calculate current stock levels by
    aggregating all "in" and "out" operations.

    Attributes:
        product (ForeignKey):
            Reference to the product affected by the movement.

        quantity (PositiveIntegerField):
            Number of units involved in the movement.

        movement_type (CharField):
            Type of movement:
                - "in": Stock is added
                - "out": Stock is removed

        reason (CharField):
            Context of the movement:
                - "purchase": Inventory received from provider
                - "sale": Product sold to customer
                - "return": Product returned
                - "adjustment": Manual correction

        performed_by (ForeignKey):
            User (employee) who performed or registered the movement.

        reference_id (CharField):
            Optional external reference identifier.
            Examples:
                - Order ID ("order_123")
                - Inventory record ID ("inventory_45")

        created_at (DateTimeField):
            Timestamp when the movement was created.

    Notes:
        - This model should be used for all stock calculations.
        - Orders and inventory records should trigger movements,
          not be used directly for stock computation.

    Example:
        Inventory arrives:
            movement_type = "in"
            quantity = 50
            reason = "purchase"

        Product sold:
            movement_type = "out"
            quantity = 2
            reason = "sale"
    """
    MOVEMENT_TYPE = [
        ("in", "In"),
        ("out", "Out"),
    ]

    REASON_TYPE = [
        ("purchase", "Purchase"),     
        ("sale", "Sale"),             
        ("return", "Return"),         
        ("adjustment", "Adjustment"), 
    ]

    product = models.ForeignKey(
        product,
        on_delete=models.CASCADE,
        related_name="inventory_movements"
    )

    quantity = models.PositiveIntegerField()

    movement_type = models.CharField(
        max_length=10,
        choices=MOVEMENT_TYPE
    )

    reason = models.CharField(
        max_length=20,
        choices=REASON_TYPE
    )

    performed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="inventory_actions",
        limit_choices_to={"role": "employee"}
    )

    reference_id = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    # Example: "order_123", "inventory_45"

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} | {self.movement_type} | {self.quantity}"