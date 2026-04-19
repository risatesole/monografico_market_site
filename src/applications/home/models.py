from django.db import models
from django.contrib.auth.models import AbstractUser


# ----------------------
# USER
# ----------------------
class User(AbstractUser):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("deactivated", "Deactivated"),
        ("deleted", "Deleted"),
    ]

    ROLE_CHOICES = [
        ("customer", "Customer"),
        ("internal_user", "Internal User"),
        ("provider", "Provider"),
    ]

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


# ----------------------
# CUSTOMER ORDER
# ----------------------
class CustomerOrder(models.Model):
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


# ----------------------
# CUSTOMER ORDER ITEM
# ----------------------
class CustomerOrderItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item {self.id}"


# ----------------------
# PRODUCT
# ----------------------
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# ----------------------
# PRODUCT LOT
# ----------------------
class ProductLot(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column="product_id"
    )

    recived_at = models.IntegerField()

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
        db_column="approved_by"
    )

    acquisition_cost_per_unit = models.FloatField()
    acquisition_tax = models.FloatField()

    received_at = models.DateTimeField()

    def __str__(self):
        return f"Lot {self.id}"


# ----------------------
# PRODUCT PURCHASE REQUISITIONS
# ----------------------
class ProductPurchaseRequisition(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="provider_id"
    )

    requested_at = models.DateTimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_estimated = models.BigIntegerField()

    def __str__(self):
        return f"Requisition {self.id}"


# ----------------------
# META REQUEST BE PROVIDER ACCOUNT
# ----------------------
class MetaRequestBeProviderAccount(models.Model):
    requested_at = models.DateTimeField()

    requested_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="provider_requests",
        db_column="requested_by"
    )

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="approved_provider_requests",
        db_column="approved_by"
    )

    def __str__(self):
        return f"Request {self.id}"


# ----------------------
# PROVIDER APPLICATION TO BE PROVIDER
# ----------------------
class ProviderApplicationToBeProvider(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("vetting", "Vetting"),
        ("approved", "Approved"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id"
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    external_id = models.CharField(max_length=255)
    notes = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application {self.id}"