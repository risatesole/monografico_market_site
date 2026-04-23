from django.contrib import admin
from .models import Product, Offer


class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]


@admin.register(Product)
class ProductAdmin(ReadOnlyAdmin):
    list_display = ("id", "name", "category")


@admin.register(Offer)
class OfferAdmin(ReadOnlyAdmin):
    list_display = ("id", "product", "providerid", "status", "priceperunit", "unitquantity", "datetime")