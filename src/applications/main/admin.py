from django.contrib import admin
from .models import Product, Offer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name", "category")
    list_filter = ("category",)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "providerid",
        "status",
        "priceperunit",
        "unitquantity",
        "datetime",
    )
    search_fields = ("providerid", "status")
    list_filter = ("status", "datetime")