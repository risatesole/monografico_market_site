from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from enum import Enum

class UserRoles(Enum):
    """Abstraction to avialable roles"""
    CUSTOMER = "customer"
    PROVIDER = "provider"
    EMPLOYEE = "employee"

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
        extra_fields.setdefault("role", "employee")

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("deactivated", "Deactivated"),
        ("deleted", "Deleted"),
    ]

    ROLE_CHOICES = [
        ("customer", "Customer"),
        ("employee", "Employee"),
        ("provider", "Provider"),
    ]

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")

    # required by Django admin/auth
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Product(models.Model):
    CATEGORY_CHOICE=[
        ("LACTEOS","Lacteos"),
        ("CARNES","carnes"),
        ("VINOS","Vinos")
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICE
    )
    image = models.ImageField(upload_to="products/", null=True, blank=True)  
    def __str__(self):
        return self.name

class Offer(models.Model):
    STATUS_CHOICE = [
        ("PENDING","Pending" ),
        ("ACCEPTED","Acepted"),
        ("DECLINED","Declined")
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    providerid = models.IntegerField()
    datetime = models.DateTimeField()
    priceperunit = models.FloatField()
    unitquantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="PENDING")

