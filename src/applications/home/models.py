from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# ----------------------
# CUSTOM USER MANAGER
# ----------------------
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("status", "active")
        extra_fields.setdefault("role", "internal_user")

        return self.create_user(email, password, **extra_fields)


# ----------------------
# USER
# ----------------------
class User(AbstractBaseUser, PermissionsMixin):
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

    # required by Django admin/auth
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

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

    recived_at = models.IntegerField()  # kept as in UML

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
# PROVIDER APPLICATION TO BE PROVIDER
# ----------------------
class ProviderApplicationToBeProvider(models.Model):
    """
    this model represents when a user a request to the provider with text that the user wants to be a provider
    
    """
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
