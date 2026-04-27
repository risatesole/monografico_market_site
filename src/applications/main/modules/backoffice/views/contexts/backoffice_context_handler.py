from ....usecases import get_all_product_sale_requests, get_all_products
from ....product.services.price.service_price import PriceService


def backoffice_view_context_handler():
    """LOAD DATA"""
    price_service = PriceService()
    offers = get_all_product_sale_requests()
    products = get_all_products()
    for product in products:
        # inject price to product data
        product.current_price = price_service.get_product_price(product) # type: ignore

    context = {
        "providers_offers": offers,
        "products": products
    }
    return context
