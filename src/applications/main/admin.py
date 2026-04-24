from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Product, Offer

# =========================
# USER ADMIN
# =========================
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    list_display = (
        "email",
        "first_name",
        "last_name",
        "role",
        "status",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "role",
        "status",
        "is_staff",
        "is_active",
        "groups",
    )

    search_fields = (
        "email",
        "first_name",
        "last_name",
    )

    ordering = ("email",)

    fieldsets = (
        ("Credentials", {
            "fields": ("email", "password")
        }),
        ("Personal Info", {
            "fields": ("first_name", "last_name")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Status & Role", {
            "fields": ("status", "role")
        }),
        ("Important Dates", {
            "fields": ("last_login",)
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "first_name",
                "last_name",
                "password1",
                "password2",
                "role",
                "status",
                "is_staff",
                "is_active",
            ),
        }),
    )


# =========================
# PRODUCT ADMIN
# =========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "image",
    )

    list_filter = ("category",)

    search_fields = ("name", "description")

    ordering = ("name",)

    readonly_fields = ("image",)

    fieldsets = (
        ("Product Info", {
            "fields": ("name", "description", "category", "image")
        }),
    )


# =========================
# OFFER ADMIN
# =========================
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "providerid",
        "datetime",
        "priceperunit",
        "unitquantity",
        "status",
    )

    list_filter = (
        "status",
        "datetime",
        "product",
    )

    search_fields = (
        "product__name",
        "providerid",
    )

    ordering = ("-datetime",)

    fieldsets = (
        ("Offer Details", {
            "fields": (
                "product",
                "providerid",
                "datetime",
                "priceperunit",
                "unitquantity",
                "status",
            )
        }),
    )