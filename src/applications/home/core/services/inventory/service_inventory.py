from django.db.models import Sum, F, Value
from django.db.models.functions import Coalesce
from ...models.model_product import Product
from ...models.model_batch import Batch
from ...models.model_selling_record_unit import UnitSellingRecordsUnits


class InventoryService:

    @staticmethod
    def list_product_stock():
        products = Product.objects.all()

        result = []

        for product in products:
            purchased = (
                Batch.objects.filter(product=product)
                .aggregate(total=Coalesce(Sum("quantity_of_units"), 0))
                ["total"]
            )

            sold = (
                UnitSellingRecordsUnits.objects.filter(
                    batchid__product=product
                )
                .aggregate(total=Coalesce(Sum("quantity_of_units"), 0))
                ["total"]
            )

            stock = purchased - sold

            result.append({
                "product_id": product.id,
                "name": product.name,
                "category": product.category,
                "stock": stock,
                "purchased": purchased,
                "sold": sold,
            })

        return result