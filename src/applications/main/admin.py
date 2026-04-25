from django.contrib import admin
from .models import Batch
from .models import User
from .models import Product
from .models import Offer
from .models import Price


# -------------------------
# Product Admin
# -------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name", "description")
    list_filter = ("category",)


# -------------------------
# Offer Admin
# -------------------------
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "provider",
        "priceperbatch",
        "batchquantity",
        "unitperbatch",
        "status",
        "datetime",
    )
    list_filter = ("status", "datetime")
    search_fields = ("product__name", "provider__email")
    autocomplete_fields = ("product", "provider")


# -------------------------
# User Admin
# -------------------------
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "role", "status", "is_staff")
    list_filter = ("role", "status", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


# -------------------------
# Batch Admin
# -------------------------
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "provider",
        "accepted_by",
        "unitperbatch",
        "acquisition_price",
        "datetime",
    )
    list_filter = ("datetime",)
    search_fields = ("product__name", "provider__email", "accepted_by__email")
    autocomplete_fields = ("product", "provider", "accepted_by")
    



    
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "value",
        "created_at",
    )

    list_filter = ("created_at",)

    search_fields = ("product__name",)

    autocomplete_fields = ("product",)