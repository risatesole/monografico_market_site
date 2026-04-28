from ...models.price_model import Price
class PriceService:
    def get_product_price(self,product):
        last_price = product.prices.first()
        return last_price.value if last_price else None

    def set_product_price(self,product,value):
        return Price.objects.create(
            product=product,
            value=value
        )
