from ..services.price.service_price import PriceService

priceservice = PriceService()

def get_product_price():
    return priceservice.get_product_price()

def set_product_price():
    return priceservice.set_product_price()
