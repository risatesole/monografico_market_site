from django.test import TestCase
from django.utils import timezone

from ...models.model_product import Product
from ...models.model_batch import Batch
from ...models.model_unit import Unit
from ...models.model_selling_record_unit import UnitSellingRecordsUnits

from .service_inventory import InventoryService


class InventoryServiceTest(TestCase):

    def setUp(self):
        # Create product
        self.product = Product.objects.create(
            name="Keyboard",
            description="Mechanical keyboard",
            category="customer"
        )

        # Create batches (total stock = 100)
        self.batch1 = Batch.objects.create(
            product=self.product,
            quantity_of_units=60,
            purchase_price=10.0
        )

        self.batch2 = Batch.objects.create(
            product=self.product,
            quantity_of_units=40,
            purchase_price=12.0
        )

        # Create units linked to batches
        self.unit1 = Unit.objects.create(batch_id=self.batch1)
        self.unit2 = Unit.objects.create(batch_id=self.batch2)

        # Create sales (total sold = 30)
        UnitSellingRecordsUnits.objects.create(
            datetime=timezone.now(),
            unitid=self.unit1,
            batchid=self.batch1,
            entity="customer",
            quantity_of_units=20,
            purchase_price=15.0
        )

        UnitSellingRecordsUnits.objects.create(
            datetime=timezone.now(),
            unitid=self.unit2,
            batchid=self.batch2,
            entity="customer",
            quantity_of_units=10,
            purchase_price=15.0
        )

    def test_inventory_stock_calculation(self):
        result = InventoryService.list_product_stock()

        self.assertEqual(len(result), 1)

        product_data = result[0]

        # 100 purchased - 30 sold = 70
        self.assertEqual(product_data["purchased"], 100)
        self.assertEqual(product_data["sold"], 30)
        self.assertEqual(product_data["stock"], 70)

        self.assertEqual(product_data["name"], "Keyboard")
