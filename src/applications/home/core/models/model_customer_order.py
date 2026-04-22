from django.db import models
from ...models import User

# ----------------------
# CUSTOMER ORDER
# ----------------------
class customer_order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("done", "Done"),
        ("canceled", "Canceled"),
    ]

    created_at = models.DateTimeField(auto_now_add=True)

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="customer_id"
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    payment_method = models.CharField(max_length=50)
    direction = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.id}"

