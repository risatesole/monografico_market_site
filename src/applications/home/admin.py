from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


# ----------------------
# USER ADMIN
# ----------------------
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "email", "first_name", "last_name", "role", "status")
    list_filter = ("role", "status")

    search_fields = ("email", "first_name", "last_name")
    ordering = ("id",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Role & Status", {"fields": ("role", "status")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "role", "status"),
        }),
    )


# ----------------------
# OTHER MODELS
# ----------------------
@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "payment_method", "created_at")
    list_filter = ("status",)
    search_fields = ("customer__email",)


@admin.register(CustomerOrderItem)
class CustomerOrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(ProductLot)
class ProductLotAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "provider",
        "approved_by",
        "acquisition_cost_per_unit",
        "received_at",
    )

    search_fields = ("product__name", "provider__email")


@admin.register(ProductPurchaseRequisition)
class ProductPurchaseRequisitionAdmin(admin.ModelAdmin):
    list_display = ("id", "provider", "status", "total_estimated", "requested_at")
    list_filter = ("status",)


@admin.register(MetaRequestBeProviderAccount)
class MetaRequestBeProviderAccountAdmin(admin.ModelAdmin):
    list_display = ("id", "requested_by", "approved_by", "requested_at")


@admin.register(ProviderApplicationToBeProvider)
class ProviderApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "external_id", "created_at")
    list_filter = ("status",)
    search_fields = ("user__email",)